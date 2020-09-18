from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        """test creating new user with email successfull"""

        email = 'cris@cris.com.br'
        password = "1234"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test the email for a new user is normalized"""

        email = 'test@CRIS.com'
        user = get_user_model().objects.create_user(email, '1234')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """TEst creating user with no email raises error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '1234')

    def test_create_new_super_user(self):
        """creating new super user'"""
        user = get_user_model().objects.create_super_user(
            "cris@cris.com",
            '1234',
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
