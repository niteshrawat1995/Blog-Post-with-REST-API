from .api_views import (PostCreateAPIView, PostListAPIView, PostDetailUpdateDeleteAPIView,
                        AuthorListAPIView, AuthorDetailAPIView
                        )

from django.urls import path

urlpatterns = [
    # api/blog/posts/show/
    path('posts/show/', PostListAPIView.as_view()),
    # api/blog/posts/2/
    path('posts/<int:pk>/show/', PostDetailUpdateDeleteAPIView.as_view()),
    #api/blog/posts/create/
    path('posts/create/', PostCreateAPIView.as_view(),),
    # api/blog/authors/show/
    path('authors/show/', AuthorListAPIView.as_view()),
    # api/blog/authors/1/show/
    path('authors/<int:pk>/show/', AuthorDetailAPIView.as_view())
    ]