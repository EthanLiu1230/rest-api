from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'ethan@gmail.com'
        password = 'abc123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'test@EthAn.cOm'
        user = get_user_model().objects.create_user(email,'123abc')

        self.assertEqual(user.email, email.lower())

