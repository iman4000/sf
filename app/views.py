from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import TemplateView
from persiantools.jdatetime import JalaliDateTime

from .models import Available, Received, Delivery


class IndexView(TemplateView):

    def get(self, request):
        context = {
            'count_available': Available.objects.count(), 
            'count_received': Received.objects.count(), 
            'count_delivery': Delivery.objects.count(),
            }
        return render(request, 'app/index.html', context)


class AvailableListView(LoginRequiredMixin, ListView):

    model = Available
    paginate_by = 100
    template_name = 'app/available_list.html'


    def get_queryset(self):
        filter_val = self.request.GET.get('filter', '')
        new_context = Available.objects.filter(
            Q(fireWall__vendor__icontains=filter_val) | Q(fireWall__brand__icontains=filter_val) | Q(fireWall__model__icontains=filter_val) | Q(fireWall__version__icontains=filter_val) | Q(fireWall__sn__icontains=filter_val) | Q(replace__icontains=filter_val) | Q(action__icontains=filter_val) | Q(replace__icontains=filter_val) | Q(action__icontains=filter_val)
        ).order_by('-created_date')
        return new_context

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter', '')
        return context


class ReceivedListView(LoginRequiredMixin, ListView):
    
    model = Received
    paginate_by = 100
    template_name = 'app/delivery_list.html'

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', '')
        new_context = Received.objects.filter(
            Q(fireWall__vendor__icontains=filter_val) | Q(fireWall__brand__icontains=filter_val) | Q(fireWall__model__icontains=filter_val) | Q(fireWall__version__icontains=filter_val) | Q(fireWall__sn__icontains=filter_val) | Q(received_from_category__icontains=filter_val) |\
            Q(fibr_port_num__icontains=filter_val) | Q(eth_port_num__icontains=filter_val) | Q(device_bog__device_bog__icontains=filter_val) | Q(devilery_person_name__delivery_person__icontains=filter_val) | Q(received_person_name__recieved_person__icontains=filter_val) | Q(company__icontains=filter_val) |\
            Q(delivery_row__icontains=filter_val) |  Q(status__status__icontains=filter_val)
        ).order_by('-created_date')
        return new_context

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter', '')
        for obj in context['object_list']:
            try:
                obj.delivery_to_category_date = JalaliDateTime(obj.delivery_to_category_date).strftime("%c")
            except:
                pass
            try:
                obj.date = JalaliDateTime(obj.date).strftime("%c")
            except:
                pass
        return context


class DeliveryListView(LoginRequiredMixin, ListView):
    
    model = Delivery
    paginate_by = 100
    template_name = 'app/received_list.html'

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', '')
        new_context = Received.objects.filter(
            Q(fireWall__vendor__icontains=filter_val) | Q(fireWall__brand__icontains=filter_val) | Q(fireWall__model__icontains=filter_val) | Q(fireWall__version__icontains=filter_val) | Q(fireWall__sn__icontains=filter_val) | \
            Q(status__status__icontains=filter_val)
        ).order_by('-created_date')
        return new_context

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter', '')
        for obj in context['object_list']:
            try:
                obj.send_to_company_date = JalaliDateTime(obj.send_to_company_date).strftime("%c")
            except:
                pass
            try:
                obj.received_date = JalaliDateTime(obj.received_date).strftime("%c")
            except:
                pass
        return context