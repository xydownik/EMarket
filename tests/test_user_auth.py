import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'market.settings')


from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()
class UserAuthenticationTests(TestCase):
    databases = {'default', 'replica2'}
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email= 'test@gmail.com',
            password='testpass',
            first_name='firstname',
            last_name='lastname')

    def test_user_login_valid(self):
        """Test logging in with valid credentials"""
        login = self.client.login(email='admin@gmail.com', password='admin')
        self.assertTrue(login)

    def test_user_login_invalid(self):
        """Test logging in with invalid credentials"""
        login = self.client.login(email='test@gmail.com', password='wrongpass')
        self.assertFalse(login)

    def test_user_creation(self):
        """Test creating a user"""
        user = User.objects.create_user(
            username='newuser',
            email= 'new@gmail.com',
            password='newpass',
            first_name='newfirstname',
            last_name='newlastname')
        self.assertEqual(user.email, 'new@gmail.com')
