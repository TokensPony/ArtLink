from rest_framework import serializers
from models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

class InternalCommissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Commission
        fields = ('id', 'commtype', 'description', 'price_min', 'price_max', 'slots')

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    commissions = InternalCommissionSerializer(read_only = True, many = True)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'commstatus', 'description', 'artstyle', 'willdraw', 'wontdraw', 'img', 'commissions')

    class JSONAPIMeta:
        included_resources = ['user', 'commissions']

class CommissionSerializer(serializers.ModelSerializer):
    #profile = ProfileSerializer()
    included_serializers = {'profile': ProfileSerializer, }
    class Meta:
        model = Commission
        #fields = ('id', 'profile', 'commtype', 'description', 'price_min', 'price_max', 'slots')
        fields = '__all__'

    class JSONAPIMeta:
        included_resources = ['profile']

    #def create(self, validated_data):
    #    #profile_data = validated_data.pop('profile')
    #    print(validated_data)
#    return Commission.objects.create(**validated_data)
