import pytz
from django.contrib import admin

from jalali_date.admin import ModelAdminJalaliMixin
from jalali_date import datetime2jalali

from . import models


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display_links = (
        'name',
        )
    list_display = (
        'id',
        'name',
        )


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display_links = (
        'name',
        )
    list_display = (
        'id',
        'name',
        )


@admin.register(models.Firewall)
class FirewallAdmin(admin.ModelAdmin):
    list_display_links = (
        'id',
        )
    list_display = (
        'id',
        'vendor',
        'brand',
        'model',
        'version',
        'sn',
        )
    search_fields = (
        'vendor',
        'brand',
        'model',
        'version',
        'sn',
    )


@admin.register(models.FirewallChange)
class FirewallChangeAdmin(admin.ModelAdmin):
    list_display_links = (
        'id',
        )
    list_display = (
        'id',
        'old_firewall',
        'change_description',
        )


@admin.register(models.Available)
class AvailableAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    def date_get_persian(self, obj):
        try:
            return datetime2jalali(obj.created_date).strftime('%Y/%m/%d %H:%M')
        except:
            return ""

    raw_id_fields = (
        'firewall',
        )
    list_display_links = (
        'id',
        )
    list_display = (
        'id',
        'firewall',
        'action',
        'date_get_persian',
        )
    date_get_persian.short_description = 'date'


@admin.register(models.DeliveryToCategory)
class DeliveryToCategoryAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    def date_get_persian(self, obj):
        try:
            return datetime2jalali(obj.date).strftime('%Y/%m/%d %H:%M')
        except:
            return ""

    raw_id_fields = (
        'firewall',
        )
    list_display_links = (
        'id',
        )
    list_display = (
        'id',
        'firewall',
        'category',
        'action',
        'delivery_person',
        'date_get_persian',
        'status',
        )
    date_get_persian.short_description = 'date'


@admin.register(models.DeliveryToCompany)
class DeliveryToCompanyAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    def date_get_persian(self, obj):
        try:
            return datetime2jalali(obj.date).strftime('%Y/%m/%d %H:%M')
        except:
            return ""

    raw_id_fields = (
        'firewall',
        )
    list_display_links = (
        'id',
        )
    list_display = (
        'id',
        'firewall',
        'company',
        'action',
        'delivery_person',
        'company_person',
        'date_get_persian',
        'status',
        )
    date_get_persian.short_description = 'date'


@admin.register(models.ReceivedFromCategory)
class ReceivedFromCategoryAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    def date_get_persian(self, obj):
        try:
            return datetime2jalali(obj.date).strftime('%Y/%m/%d %H:%M')
        except:
            return ""

    raw_id_fields = (
        'firewall',
        )
    list_display_links = (
        'id',
        )
    list_display = (
        'id',
        'firewall',
        'category',
        'device_problem',
        'received_person',
        'date_get_persian',
        'status',
        )
    date_get_persian.short_description = 'date'


@admin.register(models.ReceivedFromCompany)
class ReceivedFromCompanyAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    def date_get_persian(self, obj):
        try:
            return datetime2jalali(obj.date).strftime('%Y/%m/%d %H:%M')
        except:
            return ""

    raw_id_fields = (
        'firewall',
        'firewall_changes',
        )
    list_display_links = (
        'id',
        )
    list_display = (
        'id',
        'firewall',
        'company',
        'firewall_changes',
        'device_problem',
        'company_person',
        'received_person',
        'date_get_persian',
        'status',
        )
    date_get_persian.short_description = 'date'


@admin.register(models.Status)
class StatusAdmin(admin.ModelAdmin):
    list_display_links = (
        'name',
        )
    list_display = (
        'id',
        'name',
        )


@admin.register(models.DeviceProblem)
class DeviceProblemAdmin(admin.ModelAdmin):
    list_display_links = (
        'name',
        )
    list_display = (
        'id',
        'name',
        'description',
        )


@admin.register(models.CompanyPerson)
class CompanyPersonAdmin(admin.ModelAdmin):
    list_display_links = (
        'name',
        )
    list_display = (
        'id',
        'name',
        'phone_number',
        )


@admin.register(models.Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display_links = (
        'name',
        )
    list_display = (
        'id',
        'name',
        'phone_number',
        )


@admin.register(models.Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display_links = (
        'id',
        )
    list_display = (
        'id',
        'firwall_get_name',
        'received_from_category',
        'delivery_to_company',
        'received_from_company',
        'delivery_to_category'
        )
    raw_id_fields = (
        'received_from_category',
        'delivery_to_company',
        'received_from_company',
        'delivery_to_category'
        )

    def firwall_get_name(self, obj):
        if obj.received_from_category:
            try:
                return u"" \
                    + obj.received_from_category.firewall.vendor \
                    + " " + obj.received_from_category.firewall.brand \
                    + " " + obj.received_from_category.firewall.model \
                    + " V:" + obj.received_from_category.firewall.version \
                    + " SN:" + obj.received_from_category.firewall.sn 
            except:
                return u"" 
        elif obj.delivery_to_company:
            try:
                return u"" \
                    + obj.delivery_to_company.firewall.vendor \
                    + " " + obj.delivery_to_company.firewall.brand \
                    + " " + obj.delivery_to_company.firewall.model \
                    + " V:" + obj.delivery_to_company.firewall.version \
                    + " SN:" + obj.delivery_to_company.firewall.sn 
            except:
                return u"" 
        elif obj.received_from_company:
            try:
                return u"" \
                    + obj.received_from_company.firewall.vendor \
                    + " " + obj.received_from_company.firewall.brand \
                    + " " + obj.received_from_company.firewall.model \
                    + " V:" + obj.received_from_company.firewall.version \
                    + " SN:" + obj.received_from_company.firewall.sn 
            except:
                return u"" 
        elif obj.delivery_to_category:
            try:
                return u"" \
                    + obj.delivery_to_category.firewall.vendor \
                    + " " + obj.delivery_to_category.firewall.brand \
                    + " " + obj.delivery_to_category.firewall.model \
                    + " V:" + obj.delivery_to_category.firewall.version \
                    + " SN:" + obj.delivery_to_category.firewall.sn 
            except:
                return u"" 
        else:
            return u"" 
    
    firwall_get_name.short_description = 'firewall'