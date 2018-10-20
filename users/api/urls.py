from users.api.api_views import ProfileListAPIView, ProfileDetailAPIView
from django.urls import path


urlpatterns = [
    #/api/users/profile/show/
    path('profile/show/', ProfileListAPIView.as_view(), name='users-list'),
    #api/users/profile/1/show/
    path('profile/<int:user>/show/', ProfileDetailAPIView.as_view(), name='users-detail'),
]
