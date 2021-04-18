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
        filter = request.GET.get('filter', '')
        if filter == '':
            available = Available.objects.all()
            delivery_to_company = DeliveryToCompany.objects.all()
            delivery_to_category = DeliveryToCategory.objects.all()
            received_to_company = ReceivedFromCompany.objects.all()
            received_to_category = ReceivedFromCategory.objects.all()
        else:
            pass
        data = {
            available: available,
            delivery_to_company: delivery_to_company, 
            delivery_to_category: delivery_to_category, 
            received_to_company: received_to_company, 
            received_to_category: received_to_category
            }
        return render(request, 'app/search.html', context = data)
