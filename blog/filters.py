import django_filters
from .models import Post


class ProductFilter(django_filters.FilterSet):


    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'date_posted', 'author']
