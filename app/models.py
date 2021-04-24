from django.db import models
from django.core.validators import RegexValidator

class Category(models.Model):
    category = models.CharField(max_length=300)

    def __str__(self):
        return self.category

class FireWall(models.Model):
    vendor = models.CharField(max_length=300)
    brand = models.CharField(max_length=300)
    model = models.CharField(max_length=300)
    version = models.CharField(max_length=300)
    sn= models.CharField(max_length=300)
    def __str__(self):
         return '%s (%s) - %s' % (self.brand, self.model, self.sn)


class Available(models.Model):
    action = models.CharField(max_length=300)
    replace = models.CharField(max_length=300)
    fireWall = models.ForeignKey('FireWall',on_delete=models.CASCADE,null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add = True, editable = False)

    def __str__(self):
         return '%s (%s)' % (self.fireWall.brand,self.fireWall.model)


class Received(models.Model):
    category = models.ForeignKey('Category',on_delete=models.CASCADE,null=True,blank=True)
    fireWall = models.ForeignKey('FireWall',on_delete=models.CASCADE,null=True,blank=True)
    fibr_port_num = models.CharField(max_length=300)
    eth_port_num = models.CharField(max_length=300)
    device_bog = models.ForeignKey('Device', on_delete=models.CASCADE, null=True, blank=True)
    devilery_person_name = models.ForeignKey('DeliveryPerson', on_delete=models.CASCADE, null=True, blank=True)
    received_person_name = models.ForeignKey('RecievedPerson', on_delete=models.CASCADE, null=True, blank=True)
    received_date = models.DateTimeField(null=True, blank=True)
    send_to_company_date = models.DateTimeField(null=True, blank=True)
    company = models.CharField(max_length=300)
    status = models.ForeignKey('Status',on_delete=models.CASCADE,null=True,blank=True)
    description = models.CharField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add = True, editable = False)

    class Meta:
        abstract = True
        
    def __str__(self):
        return self.category.category


class ReceivedFromCompany(Received):
    pass


class ReceivedFromCategory(Received):
    pass


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
    phone_regex = RegexValidator(
        regex = r'^09\d{9}$',
        message = "Phone number must be entered in the format: '09XXXXXXXXX'. \"09\" than 9 digit digits allowed."
    )
    phone_number = models.CharField(
        validators = [phone_regex],
        max_length = 11, 
        null = False, 
        blank = False
    )

    def __str__(self):
        return "%s (%s)" % (self.delivery_person, self.phone_number)


class RecievedPerson(models.Model):
    recieved_person = models.CharField(max_length=200)

    def __str__(self):
        return self.recieved_person


class Delivery(models.Model):
    fireWall = models.ForeignKey('FireWall',on_delete=models.CASCADE,null=True,blank=True)
    action = models.CharField(max_length=300)
    date = models.DateTimeField(null=True, blank=True)
    name_phone = models.ForeignKey('DeliveryPerson',on_delete=models.CASCADE,null=True,blank=True)
    delivery_to_category_date = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,null=True,blank=True)
    status = models.ForeignKey('Status',on_delete=models.CASCADE,null=True,blank=True)
    description = models.CharField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add = True, editable = False)

    def __str__(self):
        return self.category.category


class DeliveryToCompany(Delivery):
    pass


class DeliveryToCategory(Delivery):
    pass
