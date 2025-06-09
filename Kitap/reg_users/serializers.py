from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import serializers

from .models import Profile, Selected, Readlater, Reading, History, Purchases


class ProfileSerializers:
    class Meta:
        model = Profile
        fields = ['contact', 'address', 'bio', 'status', 'image']


class UserSerializers(serializers.ModelSerializer):
    profile = ProfileSerializers()

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'profile']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user

class SelectedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selected
        fields = '__all__'


class ReadlaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Readlater
        fields = '__all__'

class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

class PurchasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchases
        fields = '__all__'