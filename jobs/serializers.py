from rest_framework import serializers

from jobs.models import OpportunityRequest, Opportunity


class OpportunityRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpportunityRequest
        exclude = ['id']


class OpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        exclude = ['id']
