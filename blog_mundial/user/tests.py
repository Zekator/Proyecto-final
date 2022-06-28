from django.test import TestCase
import string
import random

from forms import UserRegisterForm  
from models import User
# Create your tests here.

class TestRegister(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            
    
    
    def test_register_form(self):
        form = UserRegisterForm()
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['username'], '')
        self.assertEqual(form.cleaned_data['password'], '')
        self.assertEqual(form.cleaned_data['email'], '')
        self.assertEqual(form.cleaned_data['first_name'], '')
        self.assertEqual(form.cleaned_data['last_name'], '')
        

