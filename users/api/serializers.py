from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        from users.models import Profile

        model = Profile
        fields = ['id', 'user', 'image']
