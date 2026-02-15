import factory
from django.contrib.auth import get_user_model

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()  

    email = factory.Faker('email')  
    password = factory.PostGenerationMethodCall('set_password', 'password123')  
    is_active = True
    is_staff = False
