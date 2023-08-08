import factory

from backend.models import SaleOpportunity
from backend.tests.factories import CustomerFactory, UserFactory


class SaleOpportunityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SaleOpportunity

    customer = factory.SubFactory(CustomerFactory)
    salesperson = factory.SubFactory(UserFactory)
