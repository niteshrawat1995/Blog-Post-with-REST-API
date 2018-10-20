from rest_framework.generics import ListAPIView, RetrieveAPIView


class ProfileListAPIView(ListAPIView):
    from users.models import Profile
    from .serializers import ProfileSerializer

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetailAPIView(RetrieveAPIView):
    from users.models import Profile
    from .serializers import ProfileSerializer

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'user'
