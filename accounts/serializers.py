from rest_framework import serializers

from accounts.models import User, UserProfile, EmployerProfile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'is_employer', 'userprofile', 'employerprofile', 'password']
        read_only_fields = ['userprofile', 'employerprofile']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_employer': {'required': True}
        }

    def to_representation(self, instance):
        data = super(UserSerializer, self).to_representation(instance)
        if instance.is_employer:
            data.pop('userprofile')
        else:
            data.pop('employerprofile')
        return data


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['id', 'user']


class UserProfileSerializer(ProfileSerializer):
    class Meta(ProfileSerializer.Meta):
        model = UserProfile


class EmployerProfileSerializer(ProfileSerializer):
    class Meta(ProfileSerializer.Meta):
        model = EmployerProfile
