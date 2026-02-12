from django.test import SimpleTestCase
from .calc import add_two_number

class TestFunctioAdd(SimpleTestCase):
    
    def test_function(self):
        result = add_two_number(7, 10) 
        self.assertEqual(result,17)
    def test_wrong_num(self):
        result = add_two_number(1,7)
        self.assertNotEqual(result,2)
