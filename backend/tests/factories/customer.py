import factory

from backend.models import Customer


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    email = factory.Sequence(lambda n: f"email{n}@mail.com")
    name = factory.Faker("last_name")
