from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import TemplateView, ListView

from jalali_date import datetime2jalali

from .models import Available, Operation, ReceivedFromCategory,\
    ReceivedFromCompany, DeliveryToCategory , DeliveryToCompany


class IndexView(LoginRequiredMixin, TemplateView):

    def get(self, request):
        context = {
            'count_available': Available.objects.count(), 
            'count_operation': Operation.objects.count(), 
            'count_received_from_category': ReceivedFromCategory.objects.count(), 
            'count_delivery_to_company': DeliveryToCompany.objects.count(), 
            'count_received_from_company': ReceivedFromCompany.objects.count(), 
            'count_delivery_to_category': DeliveryToCategory.objects.count(), 
            }
        return render(request, 'app/index.html', context)


class AvailableListView(LoginRequiredMixin, ListView):
    model = Available

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['object_list'] = Available.objects.all().order_by('-created_date')
        for item in context['object_list']:
            item.created_date = datetime2jalali(item.created_date).strftime('%Y/%m/%d-%H:%M')
        return context


class ReceivedFromCategoryListView(LoginRequiredMixin, ListView):
    model = ReceivedFromCategory

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['object_list'] = ReceivedFromCategory.objects.all().order_by('-date')
        for item in context['object_list']:
            item.date = datetime2jalali(item.date).strftime('%Y/%m/%d-%H:%M')
        return context


class DeliveryToCompanyListView(LoginRequiredMixin, ListView):
    model = DeliveryToCompany

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['object_list'] = DeliveryToCompany.objects.all().order_by('-date')
        for item in context['object_list']:
            item.date = datetime2jalali(item.date).strftime('%Y/%m/%d-%H:%M')
        return context


class ReceivedFromCompanyListView(LoginRequiredMixin, ListView):
    model = ReceivedFromCompany

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['object_list'] = ReceivedFromCompany.objects.all().order_by('-date')
        for item in context['object_list']:
            item.date = datetime2jalali(item.date).strftime('%Y/%m/%d-%H:%M')
        return context


class DeliveryToCategoryListView(LoginRequiredMixin, ListView):
    model = DeliveryToCategory

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['object_list'] = DeliveryToCategory.objects.all().order_by('-date')
        for item in context['object_list']:
            item.date = datetime2jalali(item.date).strftime('%Y/%m/%d-%H:%M')
        return context


class SearchView(LoginRequiredMixin, ListView):
    model = Operation

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['object_list'] = Operation.objects.all().order_by('-created_date')
        
        for item in context['object_list']:
            
            if item.received_from_category is not None:
                # check for received_from_category
                item.received_from_category_status = True
                # Make dates jalali
                item.received_from_category.date = datetime2jalali(item.received_from_category.date).strftime('%Y/%m/%d-%H:%M')
                # Find firewall
                try:
                    item.firewall = item.received_from_category.firewall
                except:
                    pass
            else:
                # check for received_from_category
                item.received_from_category_status = False
                # set firewall to None
                item.firewall = None
            if item.delivery_to_company is not None:
                # check for delivery_to_company
                item.delivery_to_company_status = True
                # Make dates jalali
                item.delivery_to_company.date = datetime2jalali(item.delivery_to_company.date).strftime('%Y/%m/%d-%H:%M')
                # Find firewall
                if item.firewall is None:
                    try:
                        item.firewall = item.delivery_to_company.firewall
                    except:
                        pass
            else:
                # check for delivery_to_company
                item.delivery_to_company_status = False
            if item.received_from_company is not None:
                # check for received_from_company
                item.received_from_company_status = True
                # Make dates jalali
                item.received_from_company.date = datetime2jalali(item.received_from_company.date).strftime('%Y/%m/%d-%H:%M')
                # Find new_firewall, and changes
                try:
                    item.new_firewall = item.received_from_company.firewall
                    item.change_description = item.received_from_company.firewall_change.change_description
                except:
                    pass
            else:
                # check for received_from_company
                item.received_from_company_status = False
                # make a new firewall
                item.new_firewall = None
            if item.delivery_to_category is not None:
                # check for delivery_to_category
                item.delivery_to_category_status = True
                # Make dates jalali
                item.delivery_to_category.date = datetime2jalali(item.delivery_to_category.date).strftime('%Y/%m/%d-%H:%M')
            else:
                # check for delivery_to_category
                item.delivery_to_category_status = False
            # check for firewall changes
            if item.new_firewall is not None and\
                item.firewall is not None and\
                item.firewall != item.new_firewall:
                item.firewall_change_status = True
            else:
                item.firewall_change_status = False
        return context
