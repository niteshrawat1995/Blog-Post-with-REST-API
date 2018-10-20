from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        from django.contrib.auth.models import User

        model = User
        fields = ['id', 'username']


class ProfileSerializer(serializers.ModelSerializer):
    username = UserSerializer(many=False)

    class Meta:
        from users.models import Profile

        model = Profile
        fields = ['id', 'user', 'image', 'username']


