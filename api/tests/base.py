from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient

from crm.urls import API_PATH


class APITestCase(TestCase):
    @staticmethod
    def get_authenticated_api_client(user: User):
        api_client = APIClient()
        api_client.force_authenticate(user=user)
        return api_client

    def get_customers(self, salesperson: User):
        api_client = self.get_authenticated_api_client(salesperson)
        return api_client.get(f"/{API_PATH}/customers/")

    def create_customer(self, salesperson: User, data: dict):
        api_client = self.get_authenticated_api_client(salesperson)
        return api_client.post(
            f"/{API_PATH}/customers/",
            data=data,
            format="json",
        )

    def modify_customer(self, salesperson: User, customer_id: int, data: dict):
        api_client = self.get_authenticated_api_client(salesperson)
        return api_client.put(
            f"/{API_PATH}/customers/{customer_id}/",
            data=data,
            format="json",
        )

    def delete_customer(self, salesperson: User, customer_id: int):
        api_client = self.get_authenticated_api_client(salesperson)
        return api_client.delete(f"/{API_PATH}/customers/{customer_id}/")

    def get_sale_opportunities(self, salesperson: User):
        api_client = self.get_authenticated_api_client(salesperson)
        return api_client.get(f"/{API_PATH}/sale_opportunities/")

    def create_sale_opportunity(self, salesperson: User, data: dict):
        api_client = self.get_authenticated_api_client(salesperson)
        return api_client.post(
            f"/{API_PATH}/sale_opportunities/",
            data=data,
            format="json",
        )

    def modify_sale_opportunity(
        self, salesperson: User, sale_opportunity_id: int, data: dict
    ):
        api_client = self.get_authenticated_api_client(salesperson)
        return api_client.put(
            f"/{API_PATH}/sale_opportunities/{sale_opportunity_id}/",
            data=data,
            format="json",
        )

    def delete_sale_opportunity(self, salesperson: User, sale_opportunity_id: int):
        api_client = self.get_authenticated_api_client(salesperson)
        return api_client.delete(
            f"/{API_PATH}/sale_opportunities/{sale_opportunity_id}/"
        )
