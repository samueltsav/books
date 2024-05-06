from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve 
from .forms import CustomUserCreationForm

from .views import SignupPageView


class CustomUserTests(TestCase):
    ...


class SignupPageTests(TestCase):
    
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')

    def test_signup_form(self): # new
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self): # new
        view = resolve('/accounts/signup/')
        self.assertEqual(
        view.func.__name__,
        SignupPageView.as_view().__name__
        )