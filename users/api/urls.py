from users.api.api_views import ProfileListAPIView, ProfileDetailAPIView
from django.urls import path


urlpatterns = [
    #/api/users/show/
    path('show/', ProfileListAPIView.as_view(), name='users-list'),
    #api/users/1/
    path('<int:user>/', ProfileDetailAPIView.as_view(), name='users-detail'),
]
