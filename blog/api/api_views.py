from .serializers import PostSerializer, AuthorListSerializer, AuthorDetailSerializer
from blog.models import Post
from django.contrib.auth.models import User

from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,

)


class PostCreateAPIView(CreateAPIView):
    '''
    To create/ add a new post.
    '''
    queryset = Post
    serializer_class = PostSerializer

    # Associate the current logged in user as the author of the post.
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostListAPIView(ListAPIView):
    '''
    To create and list the Posts.
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    '''
    To retrieve , update and destroy a single post.
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # Associate the current user as the modifier of the post.
    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class AuthorListAPIView(ListAPIView):
    '''
    To List all the authors.
    '''
    queryset = User.objects.all()
    serializer_class = AuthorListSerializer


class AuthorDetailAPIView(RetrieveAPIView):
    '''
    To show author name and number of post written by him.
    '''
    queryset = User.objects.all()
    serializer_class =  AuthorDetailSerializer