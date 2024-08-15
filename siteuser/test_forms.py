
from django.test import TestCase
from django.contrib.auth.models import User
from .forms import SiteuserUpdateForm, ProfileUpdateForm
from .models import ProfileModel

class TestSiteuserUpdateForm(TestCase):

    def setUp(self):
        """
        Setup Test
        """
        self.user = User.objects.create_user(
            username='testeruser', 
            password='testerpassword', 
            email='tester@gmail.com'
        )

    def test_siteuser_update_form_valid_data(self):
        """
        Test if the SiteuserUpdateForm is valid with correct data.
        """
        form = SiteuserUpdateForm(
            data={
                'username': 'updatedusername',
                'email': 'updatedemail@gmail.com'
            }
        )
        self.assertTrue(form.is_valid())

    def test_siteuser_update_form_no_data(self):
        """
        Test if the SiteuserUpdateForm is invalid with incorrect data.
        """
        form = SiteuserUpdateForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1) 





