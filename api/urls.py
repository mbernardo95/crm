from django.urls import include, re_path

from rest_framework import routers

from api.views import CustomerViewSet, ServiceViewSet, SaleOpportunityViewSet


urlpatterns = []

# Add router views
router = routers.DefaultRouter()
router.register("customers", CustomerViewSet)
router.register("services", ServiceViewSet)
router.register("sale_opportunities", SaleOpportunityViewSet)
urlpatterns += [re_path(r"^", include(router.urls))]
