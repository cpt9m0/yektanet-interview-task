from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils import timezone

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from jobs.serializers import OpportunitySerializer
from jobs.models import Opportunity, OpportunityRequest

from accounts.permissions import OpportunityPermissions, IsEmployerOrReadOnly


class OpportunityAPI(generics.GenericAPIView):
    serializer_class = OpportunitySerializer
    permission_classes = [IsAuthenticated, OpportunityPermissions]

    def get_pk(self):
        return self.kwargs.get('pk', -1)

    def get(self, *args, **kwargs):
        """
        Gets details about the specified opportunity with pk or 404 error
        """
        opportunity = get_object_or_404(Opportunity, pk=self.get_pk())
        serializer = self.get_serializer(instance=opportunity)
        return Response(data=serializer.data)

    def post(self, *args, **kwargs):
        """
        Creates a request for an opportunity
        """
        user = self.request.user
        opportunity = get_object_or_404(Opportunity, pk=self.get_pk())
        if timezone.now() <= opportunity.expiration_date:
            obj, created = OpportunityRequest.objects.get_or_create(user=user.userprofile, opportunity=opportunity)
            serializer = self.get_serializer(instance=obj.opportunity)
            code = status.HTTP_200_OK
            if created:
                code = status.HTTP_201_CREATED
            return Response(
                data={
                    'detail': 'Successfully submitted.',
                    'opportunity': serializer.data
                },
                status=code
            )
        return Response(
            data={'detail': 'Opportunity expired.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    def put(self, *args, **kwargs):
        """
        Edits an opportunity by its employer
        """
        opportunity = get_object_or_404(Opportunity, pk=self.get_pk())
        if opportunity.employer == self.request.user.employerprofile:
            serializer = self.get_serializer(instance=opportunity, data=self.request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={'detail': 'Permission Denied'}, status=status.HTTP_403_FORBIDDEN)

    def patch(self, *args, **kwargs):
        """
        Partially edits an opportunity by its employer
        """
        opportunity = get_object_or_404(Opportunity, pk=self.get_pk())
        if opportunity.employer == self.request.user.employerprofile:
            serializer = self.get_serializer(instance=opportunity, data=self.request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={'detail': 'Permission Denied'}, status=status.HTTP_403_FORBIDDEN)


class OpportunityListCreateAPI(generics.ListCreateAPIView):
    """
    if authenticated user is an employer this lists his/her defined opportunities
    else if he/she is an user this lists some opportunities based on his/her expert area
    """
    permission_classes = [IsAuthenticated, IsEmployerOrReadOnly]
    serializer_class = OpportunitySerializer

    def get_queryset(self):
        if self.request.user.is_employer:
            return Opportunity.objects.filter(employer__user=self.request.user)
        else:
            user = self.request.user.userprofile
            expert_area_list = []
            user_expert_areas = user.expert_area.values('name')
            for ea in user_expert_areas:
                expert_area_list.append(ea['name'])
            del user_expert_areas
            recommendations = Opportunity.objects.filter(
                Q(employer__expert_area__name__in=expert_area_list)
            ).order_by('employer__expert_area')
            return recommendations

    def perform_create(self, serializer):
        serializer.save(employer=self.request.user.employerprofile)


class OpportunitySearchListAPI(generics.ListAPIView):
    """
    Lists opportunities based in q parameter.
    This checks titles, descriptions and company names
    """
    permission_classes = [AllowAny]
    serializer_class = OpportunitySerializer

    def get_queryset(self):
        q = self.request.GET.get('q')
        objects = Opportunity.objects.all()
        if q:
            objects = objects.filter(
                Q(title__contains=q) | Q(description__contains=q) | Q(employer__company_name__contains=q)
            )
        return objects
