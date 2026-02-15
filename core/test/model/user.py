from core.factory import UserFactory  
from django.test import TestCase


class TestModel(TestCase):
    def setUp(self):
        self.user = UserFactory()

    def test_model(self):

        self.assertIsNotNone(self.user.email)  
        print(self.user.email)  
 
        self.assertEqual(str(self.user), self.user.email)

        self.assertTrue(self.user.is_active) 
        self.assertFalse(self.user.is_staff)  
