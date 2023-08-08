from rest_framework.serializers import ModelSerializer

from backend.models import Customer, Service, SaleOpportunity


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "id",
            "email",
            "name",
            "phone_number",
            "company",
        ]


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = [
            "id",
            "name",
            "price",
        ]


class SaleOpportunitySerializer(ModelSerializer):
    class Meta:
        model = SaleOpportunity
        fields = [
            "id",
            "stage",
            "customer",
            "salesperson",
            "created_date",
            "last_modified_date",
            "services_of_interest",
            "feedback",
            "expected_revenue",
            "call_again_on",
        ]
