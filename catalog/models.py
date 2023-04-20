from django.db import models
from django.contrib.auth.models import User


class ServiceLine(models.Model):
    service_clothing_type = models.CharField(max_length=20)
    service_price_per_unit = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.service_clothing_type


class Service(models.Model):
    service_name = models.CharField(max_length=30)
    service_price_per_unit = models.DecimalField(max_digits=4, decimal_places=2)
    service_est_time_per_unit = models.CharField(max_length=10)

    def __str__(self):
        return self.service_name


class Order(models.Model):
    order_clothing_type = models.CharField(max_length=20)
    order_clothing_quantity = models.IntegerField()
    order_delivery_street = models.CharField(max_length=40)
    order_delivery_city = models.CharField(max_length=40)
    order_delivery_state = models.CharField(max_length=40)
    order_delivery_zipcode = models.CharField(max_length=15)
    order_delivery_contact_number = models.CharField(max_length=10)
    order_pick_up_required = models.BooleanField(False)
    order_date_created = models.DateTimeField(auto_now_add=True)
    order_estimated_completion_date = models.DateField(null=True, blank=True)
    order_sub_total = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.order_clothing_type} - {self.order_date_created}"


class Invoice(models.Model):
    invoice_date = models.DateField(null=True, blank=True)
    invoice_subtotal = models.DecimalField(max_digits=4, decimal_places=2)
    invoice_total = models.DecimalField(max_digits=4, decimal_places=2)
    invoice_tax = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"Invoice {self.id} - {self.invoice_date}"


class Customer(models.Model):
    customer_username = models.CharField(max_length=20)
    customer_password = models.CharField(max_length=20)
    customer_email = models.CharField(max_length=50)
    customer_first_name = models.CharField(max_length=40)
    customer_last_name = models.CharField(max_length=40)
    customer_street = models.CharField(max_length=50)
    customer_city = models.CharField(max_length=50)
    customer_zipcode = models.CharField(max_length=50)
    customer_phone_number = models.CharField(max_length=10)
    customer_credit_card_number = models.CharField(max_length=16)
    customer_card_expiry = models.CharField(max_length=6)
    customer_credit_card_cvv = models.IntegerField()

    def __str__(self):
        return f"{self.customer_first_name} {self.customer_last_name} - {self.customer_email}"


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=20)
    pincode = models.CharField(max_length=20)
    house_no = models.CharField(max_length=20)
    street = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.full_name}, {self.house_no}, {self.street}, {self.landmark}, {self.city}, {self.pincode}'
