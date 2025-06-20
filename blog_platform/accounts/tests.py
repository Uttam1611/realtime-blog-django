from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post
from unittest.mock import patch


class UserAuthTests(TestCase):
    def test_user_can_signup(self):
        resp = self.client.post(
            reverse('signup'),
            {'username': 'newuser', 'password1': 'Pass12345!', 'password2': 'Pass12345!'}
        )
        self.assertEqual(resp.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_user_can_login(self):
        User.objects.create_user(username='tester', password='pass')
        resp = self.client.post(reverse('login'), {'username': 'tester', 'password': 'pass'})
        self.assertEqual(resp.status_code, 302)

    def test_login_with_wrong_password(self):
        User.objects.create_user(username='tester', password='pass')
        resp = self.client.post(reverse('login'), {'username': 'tester', 'password': 'wrong'})
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Invalid username or password")

    def test_user_can_logout(self):
        user = User.objects.create_user(username='tempuser', password='pass')
        self.client.login(username='tempuser', password='pass')
        resp = self.client.get(reverse('logout'))
        self.assertEqual(resp.status_code, 302)  
        resp = self.client.get(reverse('post_list'))
        self.assertNotIn('_auth_user_id', self.client.session) 

User = get_user_model()

class PostDeleteTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='john', password='testpass'
        )
        self.client.login(username='john', password='testpass')
        self.post = Post.objects.create(
            title='Test Post', content='Test content', author=self.user
        )

    def test_delete_own_post(self):
        resp = self.client.post(
            reverse('delete_post', args=[self.post.id])
        )
        self.assertRedirects(resp, reverse('post_list'))
        self.assertFalse(
            Post.objects.filter(id=self.post.id).exists()
        )

    def test_cannot_delete_other_users_post(self):
        other_user = User.objects.create_user(
            username='other', password='pass123'
        )
        other_post = Post.objects.create(
            title='Other Post', content='Other content', author=other_user
        )
        resp = self.client.post(
            reverse('delete_post', args=[other_post.id])
        )
        self.assertEqual(resp.status_code, 403)
        self.assertTrue(
            Post.objects.filter(id=other_post.id).exists()
        )
        