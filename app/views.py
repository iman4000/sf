from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import TemplateView
from persiantools.jdatetime import JalaliDateTime

from .models import Available, DeliveryFromCompany, DeliveryFromCategory, ReceivedFromCategory, ReceivedFromCompany


class IndexView(TemplateView):

    def get(self, request):
        context = {
            'count_available': Available.objects.count(), 
            'count_received_from_category': ReceivedFromCategory.objects.count(), 
            'count_received_from_company': ReceivedFromCompany.objects.count(), 
            'count_received_from_category': DeliveryFromCategory.objects.count(), 
            'count_received_from_company': DeliveryFromCompany.objects.count(), 
            }
        return render(request, 'app/index.html', context)


class SearchView(TemplateView):
    def get(self, request):
        return render(request, 'app/search.html')
