from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .models import Post


class TestBlogViews(TestCase):

    def setUp(self):
        """
        Set up the test environment.
        """
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.post = Post(title="Blog title", author=self.user,
                         slug="blog-title",
                         content="Blog content", status=1)
        self.post.save()

    def test_render_post_detail_page(self):
        """
        Test post detail functionality
        """
        response = self.client.get(reverse(
            'post_detail', args=['blog-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Blog title", response.content)
        self.assertIn(b"Blog content", response.content)
