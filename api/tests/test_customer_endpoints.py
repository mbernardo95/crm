from backend.models import Customer
from backend.tests.factories import UserFactory, CustomerFactory


from .base import APITestCase


class TestCustomerEndpoints(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.salesperson = UserFactory()
        CustomerFactory.create_batch(size=5)

    def test_list_customer_endpoint(self):
        response = self.get_customers(salesperson=self.salesperson)
        self.assertEquals(response.status_code, 200, response.json())
        self.assertEquals(len(response.json()), 5, response.json())

    def test_create_customer_endpoint(self):
        response = self.create_customer(
            salesperson=self.salesperson,
            data=dict(
                email="customer@mail.com",
                name="Antonelli",
                phone_number="+34 612 34 56 78",
                company="Google",
            ),
        )
        self.assertEquals(response.status_code, 201, response.json())

        query = Customer.objects.filter(email="customer@mail.com")
        self.assertEquals(query.count(), 1)

        customer = query.first()
        self.assertEquals(customer.email, "customer@mail.com")
        self.assertEquals(customer.name, "Antonelli")
        self.assertEquals(customer.phone_number, "+34 612 34 56 78")
        self.assertEquals(customer.company, "Google")

    def test_modify_customer_endpoint(self):
        existing_customer = CustomerFactory(email="customer@mail.com", name="Antonelli")
        response = self.modify_customer(
            salesperson=self.salesperson,
            customer_id=existing_customer.id,
            data=dict(
                email="customer@mail.com",
                name="Antonelli Partolli",
                phone_number="+34 612 34 56 78",
                company="Google",
            ),
        )
        self.assertEquals(response.status_code, 200, response.json())

        customer = Customer.objects.get(id=existing_customer.id)
        self.assertEquals(customer.email, "customer@mail.com")
        self.assertEquals(customer.name, "Antonelli Partolli")
        self.assertEquals(customer.phone_number, "+34 612 34 56 78")
        self.assertEquals(customer.company, "Google")

    def test_delete_customer_endpoint(self):
        existing_customer = CustomerFactory(email="customer@mail.com", name="Antonelli")
        response = self.delete_customer(
            salesperson=self.salesperson,
            customer_id=existing_customer.id,
        )
        self.assertEquals(response.status_code, 204, response)

        query = Customer.objects.filter(id=existing_customer.id)
        self.assertFalse(query.exists(), 1)
