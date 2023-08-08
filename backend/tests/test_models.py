from decimal import Decimal

from django.test import TestCase

from backend.models import Service, Customer, SaleOpportunity
from backend.tests.factories import CustomerFactory, UserFactory


class ServiceTestCase(TestCase):
    def test_create_service(self):
        service = Service.objects.create(
            name="service_1",
            price=1000,
        )

        self.assertIsNotNone(service.id)
        self.assertEquals(service.name, "service_1")
        self.assertEquals(service.price, Decimal(1000))


class CustomerTestCase(TestCase):
    def test_create_customer(self):
        customer = Customer.objects.create(
            email="customer@email.com",
            name="Alex Casablanca",
        )

        self.assertIsNotNone(customer.id)
        self.assertEquals(customer.email, "customer@email.com")
        self.assertEquals(customer.name, "Alex Casablanca")


class SaleOpportunityTestCase(TestCase):
    def setUp(self):
        self.salesperson = UserFactory()
        self.customer = CustomerFactory()

    def test_create_sale_opportunity(self):
        sale_opportunity = SaleOpportunity.objects.create(
            salesperson=self.salesperson,
            customer=self.customer,
            stage=SaleOpportunity.SaleStage.NURTURING,
            feedback="Rocking it!",
            expected_revenue=15000,
        )

        self.assertIsNotNone(sale_opportunity.id)
        self.assertEquals(sale_opportunity.customer, self.customer)
        self.assertEquals(sale_opportunity.stage, "nurturing")
        self.assertEquals(sale_opportunity.feedback, "Rocking it!")
        self.assertEquals(sale_opportunity.expected_revenue, Decimal(15000))
