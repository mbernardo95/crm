from django.contrib.auth.models import User
from django.db import models


class Service(models.Model):
    """
    Offered services by the company
    """

    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    """
    Customer information
    """

    email = models.CharField(unique=True, max_length=200)
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200, blank=True, null=True)
    company = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class SaleOpportunity(models.Model):
    """
    Represent every sale opportunity with a customer
    """

    class SaleStage(models.TextChoices):
        """https://mailshake.com/blog/sales-cycle-stages/"""

        PROSPECTING = "prospecting", "Prospecting"
        CONTACTING = "contacting", "Make Contact"
        QUALIFYING = "qualifying", "Qualify your prospect"
        NURTURING = "nurturing", "Nurture your prospect"
        OFFERING = "offering", "Present your offer"
        OBJECTIONS = "objections", "Overcome objections"
        CLOSING = "closing", "Close the sale"
        CLOSED = "closed", "Closed"
        DECLINED = "declined", "Declined"

    stage = models.CharField(
        choices=SaleStage.choices,
        max_length=200,
        default=SaleStage.PROSPECTING,
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesperson = models.ForeignKey(User, on_delete=models.PROTECT)

    created_date = models.DateTimeField(auto_now=True)
    last_modified_date = models.DateTimeField(auto_now_add=True)

    # Fields addressed to collect the more information possible on the customer interaction
    services_of_interest = models.ManyToManyField(Service, blank=True)
    feedback = models.TextField(blank=True, null=True)
    expected_revenue = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True
    )
    call_again_on = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"[{self.stage}] - {self.customer}"
