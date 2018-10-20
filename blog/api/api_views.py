from .serializers import PostSerializer, AuthorListSerializer, AuthorDetailSerializer
from blog.models import Post
from django.contrib.auth.models import User

from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView,
                                     ListAPIView, RetrieveAPIView
                                     )


class PostListAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class AuthorListAPIView(ListAPIView):

    queryset = User.objects.all()
    serializer_class = AuthorListSerializer


class AuthorDetailAPIView(RetrieveAPIView):
    '''
    To show author name and number of post written by him.
    '''
    queryset = User.objects.all()
    serializer_class =  AuthorDetailSerializer