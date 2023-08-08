import factory

from backend.models import Service


class ServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Service

    name = factory.Faker("name")
    price = factory.Faker("decimal")
