from .api_views import (PostListAPIView, PostDetailAPIView,
                        AuthorListAPIView, AuthorDetailAPIView
                        )

from django.urls import path

urlpatterns = [
    # api/blog/posts/show/
    path('posts/show/', PostListAPIView.as_view()),
    # api/blog/2/
    path('<int:pk>/', PostDetailAPIView.as_view()),
    # api/blog/authors/show/
    path('authors/show/', AuthorListAPIView.as_view()),
    # api/blog/authors/1/show/
    path('authors/<int:pk>/show/', AuthorDetailAPIView.as_view())
    ]