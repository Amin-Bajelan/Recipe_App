from django.test import testcases

from .calc import add_two_number

class TestFunctioAdd(testcases):
    
    def test_function(self):
        num1 = 10
        num2 = 7
        result = add_two_number(num1,num2)
        
        self.assertequal(result,17)