from django.db import models
from django.utils import timezone
import datetime

class FireWall(models.Model):
    vendor = models.CharField(max_length=300)
    brand = models.CharField(max_length=300)
    model = models.CharField(max_length=300)
    version = models.CharField(max_length=300)
    sn= models.CharField(max_length=300)
    def __str__(self):
         return '%s (%s)' % (self.brand,self.model)

class Available(models.Model):
    action = models.CharField(max_length=300)
    replace = models.CharField(max_length=300)
    fireWall = models.ForeignKey('FireWall',on_delete=models.CASCADE,null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add = True, editable = False)

    def __str__(self):
         return '%s (%s)' % (self.fireWall.brand,self.fireWall.model)

class Received(models.Model):
    received_from_category = models.CharField(max_length=300)
    fireWall = models.ForeignKey('FireWall',on_delete=models.CASCADE,null=True,blank=True)
    fibr_port_num = models.CharField(max_length=300, default='SOME STRING')
    eth_port_num = models.CharField(max_length=300, default='SOME STRING')
    device_bog = models.ForeignKey('Device',on_delete=models.CASCADE,null=True,blank=True)
    devilery_person_name = models.ForeignKey('DeliveryPerson',on_delete=models.CASCADE,null=True,blank=True)
    received_person_name = models.ForeignKey('RecievedPerson',on_delete=models.CASCADE,null=True,blank=True)
    received_date = models.DateTimeField(auto_now_add = True, blank=True)
    send_to_company_date = models.DateTimeField(auto_now_add=True, blank=True)
    company = models.CharField(max_length=300, default='SOME STRING')
    delivery_row = models.CharField(max_length=300, default='SOME STRING')
    status = models.ForeignKey('Status',on_delete=models.CASCADE,null=True,blank=True)
    description = models.CharField(max_length=1000, default='SOME STRING')
    created_date = models.DateTimeField(auto_now_add = True, editable = False)
    def __str__(self):
        return self.received_from_category

class Status(models.Model):
    status = models.CharField(max_length=200)
    def __str__(self):
        return self.status

class Device(models.Model):
    device_bog = models.CharField(max_length=200)
    def __str__(self):
        return self.device_bog

class DeliveryPerson(models.Model):
    delivery_person = models.CharField(max_length=200)
    def __str__(self):
        return self.delivery_person

class RecievedPerson(models.Model):
    recieved_person = models.CharField(max_length=200)
    def __str__(self):
        return self.recieved_person

    # class Meta:
    #     ordering = ["model"]
    #
    # def __str__(self):
    #     return '%s (%s)' % (self.brand,self.model)





class Delivery(models.Model):

    fireWall = models.ForeignKey('FireWall',on_delete=models.CASCADE,null=True,blank=True)
    action = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    name_phone = models.ForeignKey('DeliveryPerson',on_delete=models.CASCADE,null=True,blank=True)
    delivery_to_category_date = models.DateTimeField(auto_now_add=True, blank=True)
    delivery_to_category = models.CharField(max_length=300)
    status = models.ForeignKey('Status',on_delete=models.CASCADE,null=True,blank=True)
    description = models.CharField(max_length=1000, default='SOME STRING')
    created_date = models.DateTimeField(auto_now_add = True, editable = False)

    def __str__(self):
        return self.delivery_to_category

# Create your models here.
