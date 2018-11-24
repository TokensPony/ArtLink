from rest_framework import serializers
from models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

class CommissionSerializer(serializers.ModelSerializer):
    #profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Commission
        fields = ('id', 'profile', 'commtype', 'description', 'price_min', 'price_max', 'slots')

    class JSONAPIMeta:
        included_resources = ['profile']
    """
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        commission, created = Commission.objects.update_or_create(user=user,
                            commtype=validated_data.pop('commtype'),
                            description=validated_data.pop('description'),
                            price_min=validated_data.pop('price_min'),
                            price_max=validated_data.pop('price_max'),
                            slots=validated_data.pop('slots'))
        return commission
        """

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    commissions = CommissionSerializer(read_only = True, many = True)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'commstatus', 'description', 'artstyle', 'willdraw', 'wontdraw', 'img', 'commissions')

    class JSONAPIMeta:
        included_resources = ['user', 'commissions']

    """def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        profile, created = Profile.objects.update_or_create(user=user,
                            commstatus=validated_data.pop('commstatus'),
                            description=validated_data.pop('description'),
                            artstyle=validated_data.pop('artstyle'),
                            willdraw=validated_data.pop('willdraw'),
                            wontdraw=validated_data.pop('wontdraw'))
        return profile
        """
