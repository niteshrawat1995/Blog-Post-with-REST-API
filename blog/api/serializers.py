from rest_framework import serializers

from blog.models import Post


class AuthorListSerializer(serializers.ModelSerializer):

    class Meta:
        from django.contrib.auth.models import User

        model = User
        fields = ['id', 'username']


class AuthorDetailSerializer(serializers.ModelSerializer):

    posts = serializers.StringRelatedField(many=True, read_only=True)
    posts_count = serializers.SerializerMethodField()

    class Meta:
        from django.contrib.auth.models import User

        model = User
        fields = ['id', 'username', 'posts_count', 'posts', ]

    def get_posts_count(self, obj):
        return obj.posts.count()


class PostSerializer(serializers.ModelSerializer):

    class Meta:

        model = Post
        fields = ['id', 'title', 'content', 'author', 'date_posted']
