from django.test import TestCase
from django.utils import timezone

from blog.models import Post

from django.contrib.auth.models import User

from django.urls import reverse


class TestPost(TestCase):

    def create_article(self, title='yolo', content='blahblah'):
        user = User.objects.create_user(username='john',
                                        email='jlennon@beatles.com',
                                        password='glass onion')
        return Post.objects.create(title=title, content=content, date_posted=timezone.now(), author=user)

    def test_post_create(self):
        article = self.create_article()
        self.assertEqual(article.__str__(),article.title)
        self.assertTrue(isinstance(article,Post))

    # def test_post_list_view(self):
    #     pass
