
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm, PostUpdateForm

class PostFormTests(TestCase):

    def setUp(self):
        """
        Set up the test environment.
        """
        self.user = User.objects.create_user(username='testeruser', password='testerpass')

    def test_post_form_is_valid_data(self):
        """
        Test if the PostForm is valid with correct data.
        """
        form_data = {
            'title': 'Tester Title',
            'slug': 'tester-title',
            'content': 'This is a test.',
            'status': 0, 
            'author': self.user.id
        }
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid(), msg=form.errors)

    def test_post_form_with_no_data(self):
        """
        Test if the PostForm is invalid with no data.
        """  
        form = PostForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5)  

    def test_post_form_is_invalid_data(self):
        """
        Test if the PostForm is invalid with incorrect data.
        """
        form_data = {
            'title': '',  
            'slug': 'tester-title',
            'content': 'This is a test.',
            'status': 2,  
            'author': self.user.id
        }
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        self.assertIn('status', form.errors)

    def test_post_update_form_is_valid_data(self):
        """
        Test if the PostUpdateForm is valid with correct data.
        """
        post = Post.objects.create(
            title='Real Title',
            slug='real-title',
            content='This is Real content.',
            status=0,  
            author=self.user
        )
        form_data = {
            'title': 'New Title',
            'slug': 'new-title',
            'content': 'new content.',
            'status': 1, 
            'author': self.user.id
        }
        form = PostUpdateForm(data=form_data, instance=post)
        self.assertTrue(form.is_valid(), msg=form.errors)

    def test_post_update_form_with_no_data(self):
        """
        Test if the PostUpdateForm is invalid with incorrect data.
        """   
        form = PostUpdateForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5)  

