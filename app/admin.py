from django.contrib import admin
from . import models
from jalali_date.admin import ModelAdminJalaliMixin


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(models.FireWall)
class FireWallAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Available)
class AvailableAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    pass

@admin.register(models.DeliveryToCategory)
class DeliveryToCategoryAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    pass

@admin.register(models.DeliveryToCompany)
class DeliveryToCompanyAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    pass

@admin.register(models.ReceivedFromCategory)
class ReceivedFromCategoryAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    pass

@admin.register(models.ReceivedFromCompany)
class ReceivedFromCompanyAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    pass

@admin.register(models.Status)
class StatusAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Device)
class DeviceAdmin(admin.ModelAdmin):
    pass

@admin.register(models.DeliveryPerson)
class DeliveryPersonAdmin(admin.ModelAdmin):
    pass

@admin.register(models.RecievedPerson)
class RecievedPersonAdmin(admin.ModelAdmin):
    pass

# Register your models here.
