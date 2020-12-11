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

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            is_employer=validated_data['is_employer']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['id', 'user']


class UserProfileSerializer(ProfileSerializer):
    class Meta(ProfileSerializer.Meta):
        model = UserProfile


class EmployerProfileSerializer(ProfileSerializer):
    class Meta(ProfileSerializer.Meta):
        model = EmployerProfile
