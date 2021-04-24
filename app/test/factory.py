import factory
import factory.fuzzy
from datetime import datetime, timezone
from ..models import *


class CategoryFactory(factory.django.DjangoModelFactory):
    category = factory.fuzzy.FuzzyText()

    class Meta:
        model = Category


class FirewallFactory(factory.django.DjangoModelFactory):
    vendor = factory.fuzzy.FuzzyText()
    brand = factory.fuzzy.FuzzyText()
    model = factory.fuzzy.FuzzyText()
    version = factory.fuzzy.FuzzyFloat(1.000, 100.999)
    sn = factory.fuzzy.FuzzyInteger(1111111111, 9999999999)

    class Meta:
        model = FireWall


class AvailableFactory(factory.django.DjangoModelFactory):
    action = factory.fuzzy.FuzzyText()
    replace = factory.fuzzy.FuzzyText()
    fireWall = factory.Iterator(FireWall.objects.all())
    
    class Meta:
        model = Available


class ReceivedFromCategoryFactory(factory.django.DjangoModelFactory):
    category = factory.Iterator(Category.objects.all())
    fireWall = factory.Iterator(FireWall.objects.all())
    fibr_port_num = factory.fuzzy.FuzzyText()
    eth_port_num = factory.fuzzy.FuzzyText()
    device_bog = factory.Iterator(Device.objects.all())
    devilery_person_name = factory.Iterator(DeliveryPerson.objects.all())
    received_person_name = factory.Iterator(RecievedPerson.objects.all())
    received_date = factory.fuzzy.FuzzyDateTime(datetime(2015, 01, 01) ,datetime.now(timezone.utc))
    send_to_company_date = factory.fuzzy.FuzzyDateTime(datetime(2015, 01, 01) ,datetime.now(timezone.utc))
    company = factory.fuzzy.FuzzyText()
    status = factory.Iterator(Status.objects.all())
    description = factory.fuzzy.FuzzyText()

    class Meta:
        model = ReceivedFromCompany


class ReceivedFromCompanyFactory(factory.django.DjangoModelFactory):
    category = factory.Iterator(Category.objects.all())
    fireWall = factory.Iterator(FireWall.objects.all())
    fibr_port_num = factory.fuzzy.FuzzyText()
    eth_port_num = factory.fuzzy.FuzzyText()
    device_bog = factory.Iterator(Device.objects.all())
    devilery_person_name = factory.Iterator(DeliveryPerson.objects.all())
    received_person_name = factory.Iterator(RecievedPerson.objects.all())
    received_date = factory.fuzzy.FuzzyDateTime(datetime.datetime.now(datetime.timezone.utc))
    send_to_company_date = factory.fuzzy.FuzzyDateTime(datetime.datetime.now(datetime.timezone.utc))
    company = factory.fuzzy.FuzzyText()
    status = factory.Iterator(Status.objects.all())
    description = factory.fuzzy.FuzzyText()

    class Meta:
        model = ReceivedFromCategory


class StatusFactory(factory.django.DjangoModelFactory):
    status = factory.fuzzy.FuzzyText()

    class Meta:
            model = Status


class DeviceFactory(factory.django.DjangoModelFactory):
    device_bog = factory.fuzzy.FuzzyText()

    class Meta:
            model = Device


class DeliveryPersonFactory(factory.django.DjangoModelFactory):
    delivery_person = factory.fuzzy.FuzzyText()
    phone_number = factory.fuzzy.FuzzyInteger(9111111111, 9999999999)

    class Meta:
            model = DeliveryPerson


class RecievedPersonFactory(factory.django.DjangoModelFactory):
    recieved_person = factory.fuzzy.FuzzyText()

    class Meta:
            model = RecievedPerson


class DeliveryToCompanyFactory(factory.django.DjangoModelFactory):
    fireWall = factory.Iterator(FireWall.objects.all())
    action = factory.fuzzy.FuzzyText()
    date = factory.fuzzy.FuzzyDateTime(datetime.datetime.now(datetime.timezone.utc))
    name_phone = factory.Iterator(DeliveryPerson.objects.all())
    delivery_to_category_date = factory.fuzzy.FuzzyDateTime(datetime.datetime.now(datetime.timezone.utc))
    category = factory.Iterator(Category.objects.all())
    status = factory.Iterator(Status.objects.all())
    description = factory.fuzzy.FuzzyText()

    class Meta:
            model = DeliveryToCompany


class DeliveryToCategoryFactory(factory.django.DjangoModelFactory):
    fireWall = factory.Iterator(FireWall.objects.all())
    action = factory.fuzzy.FuzzyText()
    date = factory.fuzzy.FuzzyDateTime(datetime(2015, 01, 01) ,datetime.now(timezone.utc))
    name_phone = factory.Iterator(DeliveryPerson.objects.all())
    delivery_to_category_date = factory.fuzzy.FuzzyDateTime(datetime(2015, 01, 01) ,datetime.now(timezone.utc))
    category = factory.Iterator(Category.objects.all())
    status = factory.Iterator(Status.objects.all())
    description = factory.fuzzy.FuzzyText()

    class Meta:
            model = DeliveryToCategory