from django.contrib.auth.models import User
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("email")
    username = factory.Faker("name")
    password = factory.PostGenerationMethodCall("set_password", "adm1n")
