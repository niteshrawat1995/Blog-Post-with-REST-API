"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
# For adding media routes
from django.conf import settings
from django.conf.urls.static import static
from blog.api import urls as blog_urls
from users.api import urls as users_urls

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('register1/', user_views.RegisterCreateView.as_view(), name='register-class'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('blog.urls')),
    path('api/blog/', include(blog_urls)),
    path('api/users/', include(users_urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(r'oauth/', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# include() chops off whatever part of the url have been matched upto that point and sent the remaining string to the included urls module for further processing.

'''
curl -X POST -H "Content-Type: application/json" -d '{"username": "niteshrawat", "password": "abtech123"}' http://localhost:8000/api/token/
  
curl -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU0MDIxNjYxNSwianRpIjoiYThjNjM0MWIyN2RjNDNiMTkyZTU1M2JkMWYzNzhhMjQiLCJ1c2VyX2lkIjoxfQ.4SJMSG3nbkkMmTI9_Y3itsGoj93Ryg2Rc-FM6dK_a8c","access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTQwMTMwNTE1LCJqdGkiOiI3MmY2M2NmMzQ3YjA0ODU1YThjYWI0OTk2YWFmYmI4OSIsInVzZXJfaWQiOjF9.rBWITgYKR52Zaemxs4dBuurwIxB7vLNF-" http://localhost:8000/api/blog/posts/create/  
  
'''
