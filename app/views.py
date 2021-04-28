from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import TemplateView
from persiantools.jdatetime import JalaliDateTime

from .models import Available, DeliveryToCompany, DeliveryToCategory, ReceivedFromCategory, ReceivedFromCompany


class IndexView(TemplateView):

    def get(self, request):
        context = {
            'count_available': Available.objects.count(), 
            'count_received_from_category': ReceivedFromCategory.objects.count(), 
            'count_received_from_company': ReceivedFromCompany.objects.count(), 
            'count_received_from_category': DeliveryToCategory.objects.count(), 
            'count_received_from_company': DeliveryToCompany.objects.count(), 
            }
        return render(request, 'app/index.html', context)


class SearchView(LoginRequiredMixin, TemplateView):

    def get(self, request):
        available = Available.objects.all().order_by('-created_date')
        delivery_to_company = DeliveryToCompany.objects.all().order_by('-created_date')
        delivery_to_category = DeliveryToCategory.objects.all().order_by('-created_date')
        received_from_company = ReceivedFromCompany.objects.all().order_by('-created_date')
        received_from_category = ReceivedFromCategory.objects.all().order_by('-created_date')
        res = []
        for obj in available:
            obj.type_ = "A"
            res.append(obj)
        for obj in delivery_to_company:
            obj.type_ = "DTCo"
            obj.delivery_to_category_date = JalaliDateTime(obj.delivery_to_category_date).strftime("%Y-%m-%d %H-%M")
            obj.date = JalaliDateTime(obj.date).strftime("%Y-%m-%d %H-%M")
            res.append(obj)
        for obj in delivery_to_category:
            obj.type_ = "DTCa"
            obj.delivery_to_category_date = JalaliDateTime(obj.delivery_to_category_date).strftime("%Y-%m-%d %H-%M")
            obj.date = JalaliDateTime(obj.date).strftime("%Y-%m-%d %H-%M")
            res.append(obj)
        for obj in received_from_company:
            obj.type_ = "RFCo"
            obj.received_date = JalaliDateTime(obj.received_date).strftime("%Y-%m-%d %H-%M")
            obj.send_to_company_date = JalaliDateTime(obj.send_to_company_date).strftime("%Y-%m-%d %H-%M")
            res.append(obj)
        for obj in received_from_category:
            obj.type_ = "RFCa"
            obj.received_date = JalaliDateTime(obj.received_date).strftime("%Y-%m-%d %H-%M")
            obj.send_to_company_date = JalaliDateTime(obj.send_to_company_date).strftime("%Y-%m-%d %H-%M")
            res.append(obj)
        data = {
            'res': res,
            }
        return render(request, 'app/search.html', data)
