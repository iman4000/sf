from django.contrib import admin
from . import models


@admin.register(models.FireWall)
class FireWallAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Available)
class AvailableAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    pass
    # list_display = ('model','brand')


@admin.register(models.Received)
class ReceivedAdmin(admin.ModelAdmin):
    pass
    # list_display = ('model','brand')
    # list_filter = ('model','brand')
    # fields = [('model','brand')]

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
