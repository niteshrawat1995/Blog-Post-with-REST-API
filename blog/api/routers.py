from rest_framework.routers import DefaultRouter
from blog.api.api_views import PostViewSet

router = DefaultRouter()

router.register('posts', PostViewSet, base_name='post')

for url in router.urls:
    print(url)
    print()
