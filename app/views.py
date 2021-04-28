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
        filter_val = request.GET.get('filter', '')
        if filter_val == '':
            available = Available.objects.all().order_by('-created_date')
            delivery_to_company = DeliveryToCompany.objects.all().order_by('-created_date')
            delivery_to_category = DeliveryToCategory.objects.all().order_by('-created_date')
            received_from_company = ReceivedFromCompany.objects.all().order_by('-created_date')
            received_from_category = ReceivedFromCategory.objects.all().order_by('-created_date')
        else:
            available = Available.objects.filter(
            Q(fireWall__vendor__icontains=filter_val) | Q(fireWall__brand__icontains=filter_val) | \
            Q(fireWall__model__icontains=filter_val) | Q(fireWall__version__icontains=filter_val) | \
            Q(fireWall__sn__icontains=filter_val) | Q(replace__icontains=filter_val) | \
            Q(action__icontains=filter_val) |  Q(action__icontains=filter_val)
            ).order_by('-created_date')
            delivery_to_company = DeliveryToCompany.objects.filter(
            Q(fireWall__vendor__icontains=filter_val) | Q(fireWall__brand__icontains=filter_val) | \
            Q(fireWall__model__icontains=filter_val) | Q(fireWall__version__icontains=filter_val) | \
            Q(fireWall__sn__icontains=filter_val) | Q(action__icontains=filter_val) | \
            Q(name_phone__delivery_person__icontains=filter_val) | Q(name_phone__phone_number__icontains=filter_val) | \
            Q(category__category__icontains=filter_val) | Q(status__status__icontains=filter_val) | \
            Q(description__icontains=filter_val)
            ).order_by('-created_date')
            delivery_to_category = DeliveryToCategory.objects.filter(
            Q(fireWall__vendor__icontains=filter_val) | Q(fireWall__brand__icontains=filter_val) | \
            Q(fireWall__model__icontains=filter_val) | Q(fireWall__version__icontains=filter_val) | \
            Q(fireWall__sn__icontains=filter_val) | Q(action__icontains=filter_val) | \
            Q(name_phone__delivery_person__icontains=filter_val) | Q(name_phone__phone_number__icontains=filter_val) | \
            Q(category__category__icontains=filter_val) | Q(status__status__icontains=filter_val) | \
            Q(description__icontains=filter_val)
            ).order_by('-created_date')
            received_from_company = ReceivedFromCompany.objects.filter(
            Q(category__category__icontains=filter_val) | Q(fireWall__sn__icontains=filter_val) | \
            Q(fireWall__vendor__icontains=filter_val) | Q(fireWall__brand__icontains=filter_val) | \
            Q(fireWall__model__icontains=filter_val) | Q(fireWall__version__icontains=filter_val) | \
            Q(fibr_port_num__icontains=filter_val) |  Q(eth_port_num__icontains=filter_val) | \
            Q(device_bog__device_bog__icontains=filter_val) | Q(devilery_person_name__delivery_person___icontains=filter_val) | \
            Q(devilery_person_name__phone_number___icontains=filter_val) | Q(received_person_name__recieved_person___icontains=filter_val) | \
            Q(company___icontains=filter_val) | Q(status__status___icontains=filter_val) | \
            Q(description___icontains=filter_val)
            ).order_by('-created_date')
            received_from_category = ReceivedFromCategory.objects.filter(
            Q(category__category__icontains=filter_val) | Q(fireWall__sn__icontains=filter_val) | \
            Q(fireWall__vendor__icontains=filter_val) | Q(fireWall__brand__icontains=filter_val) | \
            Q(fireWall__model__icontains=filter_val) | Q(fireWall__version__icontains=filter_val) | \
            Q(fibr_port_num__icontains=filter_val) |  Q(eth_port_num__icontains=filter_val) | \
            Q(device_bog__device_bog__icontains=filter_val) | Q(devilery_person_name__delivery_person___icontains=filter_val) | \
            Q(devilery_person_name__phone_number___icontains=filter_val) | Q(received_person_name__recieved_person___icontains=filter_val) | \
            Q(company___icontains=filter_val) | Q(status__status___icontains=filter_val) | \
            Q(description___icontains=filter_val)
            ).order_by('-created_date')
        data = {
            'available': available,
            'delivery_to_company': delivery_to_company, 
            'delivery_to_category': delivery_to_category, 
            'received_from_company': received_from_company, 
            'received_from_category': received_from_category
            }
        return render(request, 'app/search.html', data)
