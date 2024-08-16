
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm, PostUpdateForm

class PostFormTest(TestCase):
    
    def test_post_form_valid_data(self):
        """
        Test if the PostForm is valid with correct data.
        """        
        form = PostForm(data={
            'title': 'Sample Title',
            'slug': 'sample-title',
            'content': 'This is some content.',
            'status': '1', 
        })
        self.assertTrue(form.is_valid())
    
    def test_post_form_invalid_data(self):
        """
        Test if the PostForm is invalid with incorrect data.
        """        
        form = PostForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4) 

class PostUpdateFormTest(TestCase):   
    def test_post_update_form_valid_data(self):
        """
        Test if the PostUpdateForm is valid with correct data.
        """     
        user = User.objects.create(username='testuser')
        post = Post.objects.create(
            title='Original Title',
            slug='original-title',
            content='Original content.',
            status='1',
            author=user,
    )
    
        form = PostUpdateForm(data={
            'title': 'Updated Title',
            'slug': 'updated-title',
            'content': 'Updated content.',
            'status': '1',
            'author': user.id,
    }, instance=post)
    
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())
    
    def test_post_update_form_invalid_data(self):
        """
        Test if the PostForm is invalid with incorrect data.
        """ 
        form = PostUpdateForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5)


