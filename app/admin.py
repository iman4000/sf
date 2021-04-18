from django.contrib import admin
from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(models.FireWall)
class FireWallAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Available)
class AvailableAdmin(admin.ModelAdmin):
    pass

@admin.register(models.DeliveryFromCategory)
class DeliveryFromCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(models.DeliveryFromCompany)
class DeliveryFromCompanyAdmin(admin.ModelAdmin):
    pass

@admin.register(models.ReceivedFromCategory)
class ReceivedFromCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(models.ReceivedFromCompany)
class ReceivedFromCompany(admin.ModelAdmin):
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
