from rest_framework import serializers
from models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'commstatus', 'description', 'artstyle', 'willdraw', 'wontdraw')

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        profile, created = Profile.objects.update_or_create(user=user,
                            commstatus=validated_data.pop('commstatus'),
                            description=validated_data.pop('description'),
                            artstyle=validated_data.pop('artstyle'),
                            willdraw=validated_data.pop('willdraw'),
                            wontdraw=validated_data.pop('wontdraw'))
        return profile
