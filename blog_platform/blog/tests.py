from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post

class BlogPostTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='author', password='pass')
        self.other_user = User.objects.create_user(username='other', password='pass')
        self.client.login(username='author', password='pass')
        self.post = Post.objects.create(
            title='Test Post',
            content='Test Content',
            author=self.user
        )

    def test_create_post(self):
        resp = self.client.post(
            reverse('create_post'),
            {'title': 'New Post', 'content': 'New content'}
        )
        self.assertEqual(resp.status_code, 302)
        self.assertTrue(Post.objects.filter(title='New Post').exists())

    def test_edit_own_post(self):
        resp = self.client.post(
            reverse('edit_post', args=[self.post.id]),
            {'title': 'Updated title', 'content': 'Updated content'}
        )
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated title')

    def test_edit_other_users_post_forbidden(self):
        other_post = Post.objects.create(
            title='Other Post', content='Other Content', author=self.other_user
        )
        resp = self.client.post(
            reverse('edit_post', args=[other_post.id]),
            {'title': 'Hack', 'content': 'Hack'}
        )
        self.assertEqual(resp.status_code, 403)

    def test_delete_own_post(self):
        resp = self.client.post(reverse('delete_post', args=[self.post.id]))
        self.assertEqual(resp.status_code, 302)
        self.assertFalse(Post.objects.filter(id=self.post.id).exists())

    def test_delete_other_users_post_forbidden(self):
        other_post = Post.objects.create(
            title='Other Post', content='X', author=self.other_user
        )
        resp = self.client.post(reverse('delete_post', args=[other_post.id]))
        self.assertEqual(resp.status_code, 403)

    def test_view_post_list(self):
        resp = self.client.get(reverse('post_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.post.title)