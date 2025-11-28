from django.db import models
from django.contrib import admin
# Create your models here.
class Order(models.Model):
    customer_name = models.CharField(max_length=20, help_text="Enter Name")
    order_id = models.IntegerField(help_text="Enter ID")
    date_of_order = models.DateField()
    date_of_delivery = models.DateField()

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'order_id', 'date_of_order', 'date_of_delivery']
    

# Create your models here.
