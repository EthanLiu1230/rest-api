from django.test import TestCase
from app.calc import add

class CalcTest(TestCase):

    def test_add(self):
        self.assertEqual(add(3,3), 6)