from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        """aqui eu criei os usuários"""
        # adiciona ao cliente um client
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="cris@cris.com",
            password="1234"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="favaro@favaro.com",
            password="1234",
            name="Test user full name"
        )

    def test_users_listed(self):
        """test that user are listed on user page"""

        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        # aqui ele vai fazer um get no url que eu criei

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # /admin/core/user/id - é isso que ele está fazendo no reverse
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """test that create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
