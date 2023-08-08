from backend.models import Customer, SaleOpportunity
from backend.tests.factories import UserFactory, CustomerFactory, SaleOpportunityFactory


from .base import APITestCase


class TestSaleOpportunityEndpoints(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.salesperson = UserFactory()
        cls.customer = CustomerFactory()
        SaleOpportunityFactory.create_batch(
            size=5,
            salesperson=UserFactory(),
            customer=CustomerFactory(),
        )

    def test_list_sale_opportunity_endpoint(self):
        response = self.get_sale_opportunities(salesperson=self.salesperson)
        self.assertEquals(response.status_code, 200, response.json())
        self.assertEquals(len(response.json()), 5, response.json())

    def test_create_sale_opportunity_endpoint(self):
        response = self.create_sale_opportunity(
            salesperson=self.salesperson,
            data=dict(
                salesperson=self.salesperson.id,
                customer=self.customer.id,
                stage=SaleOpportunity.SaleStage.CONTACTING,
                feedback="All good",
            ),
        )
        self.assertEquals(response.status_code, 201, response.json())

        query = SaleOpportunity.objects.filter(id=response.json()["id"])
        self.assertEquals(query.count(), 1)

        sale_opportunity = query.first()
        self.assertEquals(sale_opportunity.salesperson.id, self.salesperson.id)
        self.assertEquals(sale_opportunity.customer.id, self.customer.id)
        self.assertEquals(sale_opportunity.stage, "contacting")
        self.assertEquals(sale_opportunity.feedback, "All good")

    def test_modify_sale_opportunity_endpoint(self):
        existing_sale_opportunity = SaleOpportunityFactory(feedback="Not good")
        response = self.modify_sale_opportunity(
            salesperson=self.salesperson,
            sale_opportunity_id=existing_sale_opportunity.id,
            data=dict(
                customer=self.customer.id,
                salesperson=self.salesperson.id,
                feedback="All good",
                stage=SaleOpportunity.SaleStage.CONTACTING,
            ),
        )
        self.assertEquals(response.status_code, 200, response.json())

        sale_opportunity = SaleOpportunity.objects.get(id=existing_sale_opportunity.id)
        self.assertEquals(sale_opportunity.customer.id, self.customer.id)
        self.assertEquals(sale_opportunity.salesperson.id, self.salesperson.id)
        self.assertEquals(sale_opportunity.feedback, "All good")
        self.assertEquals(sale_opportunity.stage, "contacting")

    def test_delete_sale_opportunity_endpoint(self):
        existing_sale_opportunity = SaleOpportunityFactory(feedback="Not good")
        response = self.delete_sale_opportunity(
            salesperson=self.salesperson,
            sale_opportunity_id=existing_sale_opportunity.id,
        )
        self.assertEquals(response.status_code, 204, response)

        query = SaleOpportunity.objects.filter(id=existing_sale_opportunity.id)
        self.assertFalse(query.exists(), 1)
