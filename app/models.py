from django.db import models
from django.core.validators import RegexValidator


class Company(models.Model):
    name = models.CharField(max_length=300, null=False, blank=False, unique=True)

    def __str__(self):
        return "{}".format(self.name)


class Category(models.Model):
    name = models.CharField(max_length=300, null=False, blank=False, unique=True)

    def __str__(self):
        return "{}".format(self.name)


class Status(models.Model):
    name = models.CharField(max_length=300, null=False, blank=False, unique=True)

    def __str__(self):
        return "{}".format(self.name)


class DeviceProblem(models.Model):
    name = models.CharField(max_length=300, null=False, blank=False, unique=True)
    description = models.TextField(null=True , blank=True)
    
    def __str__(self):
        return "{}".format(self.name)


class Person(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
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

    class Meta:
        abstract = True

    def __str__(self):
        if not self.phone_number:
            return "{}".format(self.name)
        else:
            return "{} - {}".format(self.name, self.phone_number)


class Staff(Person):
    name = models.CharField(max_length=200)
    phone_regex = RegexValidator(
        regex = r'^09\d{9}$',
        message = "Phone number must be entered in the format: '09XXXXXXXXX'. \"09\" than 9 digit digits allowed."
    )
    phone_number = models.CharField(
        validators = [phone_regex],
        max_length = 11, 
        null = True, 
        blank = True
    )


class CompanyPerson(Person):
    name = models.CharField(max_length=200)
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
    company = models.ForeignKey('Company', on_delete=models.PROTECT, null=True, blank=True)


class Firewall(models.Model):
    vendor = models.CharField(max_length=300)
    brand = models.CharField(max_length=300)
    model = models.CharField(max_length=300)
    version = models.CharField(max_length=300)
    sn = models.CharField(max_length=300, null=False, blank=False, unique=True)
    fiber_port_num = models.CharField(max_length=300)
    eth_port_num = models.CharField(max_length=300)

    def __str__(self):
        return "{} - {} - {} - V:{} - SN:{}".format(self.vendor, self.brand, self.model, self.version, self.sn)


class FirewallChange(models.Model):
    change_description = models.TextField(blank=True)
    old_firewall = models.ForeignKey('Firewall', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return "id: {}".format(self.id)


class Available(models.Model):
    firewall = models.ForeignKey('Firewall', on_delete=models.PROTECT, null=False, blank=False)
    action = models.CharField(max_length=300)
    created_date = models.DateTimeField(auto_now_add = True, editable = False)

    def __str__(self):
        return "Firewall: {} - {}".format(self.firewall, self.action)


class ReceivedFromCategory(models.Model):
    firewall = models.ForeignKey('Firewall', on_delete=models.PROTECT, null=False, blank=False)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    device_problem = models.ForeignKey('DeviceProblem', on_delete=models.SET_NULL, null=True, blank=True)
    received_person = models.ForeignKey('Staff', on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    status = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return "id: {} - Firewall SN: {} - {}".format(self.id, self.firewall.sn, self.category)


class DeliveryToCompany(models.Model):
    firewall = models.ForeignKey('Firewall', on_delete=models.PROTECT, null=False, blank=False)
    action = models.CharField(max_length=300)
    date = models.DateTimeField(null=True, blank=True)
    delivery_person = models.ForeignKey('Staff', on_delete=models.SET_NULL, null=True, blank=True)
    company_person = models.ForeignKey('CompanyPerson', on_delete=models.SET_NULL, null=True, blank=True)
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return "id: {} - Firewall SN: {} - {}".format(self.id, self.firewall.sn, self.company)


class ReceivedFromCompany(models.Model):
    firewall = models.ForeignKey('Firewall', on_delete=models.PROTECT, null=False, blank=False)
    firewall_changes = models.ForeignKey('FirewallChange', on_delete=models.PROTECT, null=True, blank=True)
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, blank=True)
    device_problem = models.ForeignKey('DeviceProblem', on_delete=models.SET_NULL, null=True, blank=True)
    company_person = models.ForeignKey('CompanyPerson', on_delete=models.SET_NULL, null=True, blank=True)
    received_person = models.ForeignKey('Staff', on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    status = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return "id: {} - Firewall SN: {} - {}".format(self.id, self.firewall.sn, self.company)


class DeliveryToCategory(models.Model):
    firewall = models.ForeignKey('Firewall', on_delete=models.PROTECT, null=False, blank=False)
    action = models.CharField(max_length=300)
    date = models.DateTimeField(null=True, blank=True)
    delivery_person = models.ForeignKey('Staff', on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return "id: {} - Firewall SN: {} - {}".format(self.id, self.firewall.sn, self.category)


class Operation(models.Model):
    received_from_category = models.ForeignKey('ReceivedFromCategory', on_delete=models.PROTECT, null=True, blank=True)
    delivery_to_company = models.ForeignKey('DeliveryToCompany', on_delete=models.PROTECT, null=True, blank=True)
    received_from_company = models.ForeignKey('ReceivedFromCompany', on_delete=models.PROTECT, null=True, blank=True)
    delivery_to_category = models.ForeignKey('DeliveryToCategory', on_delete=models.PROTECT, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add = True, editable = False)

    def __str__(self):
        return "id: {}".format(self.id)