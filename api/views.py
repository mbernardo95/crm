from rest_framework.viewsets import ModelViewSet

from backend.models import Customer, Service, SaleOpportunity

from api.serializers import (
    CustomerSerializer,
    ServiceSerializer,
    SaleOpportunitySerializer,
)


class CustomerViewSet(ModelViewSet):
    """
    Create, retrieve, update, and delete customer records.
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ServiceViewSet(ModelViewSet):
    """
    Create, retrieve, update, and delete service records.
    """

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class SaleOpportunityViewSet(ModelViewSet):
    """
    Create, retrieve, update, and delete service records.
    """

    queryset = SaleOpportunity.objects.all()
    serializer_class = SaleOpportunitySerializer
