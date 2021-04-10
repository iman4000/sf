from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .models import Available, Received, Delivery


"""
@login_required
def index(request):
    return render(request, 'app/index.html')
"""
class AvailableListView(LoginRequiredMixin, ListView):

    model = Available
    paginate_by = 100

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
        return context


class DeliveryListView(LoginRequiredMixin, ListView):
    
    model = Delivery
    paginate_by = 100

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', '')
        new_context = Received.objects.filter(
            Q(fireWall__vendor__icontains=filter_val) | Q(fireWall__brand__icontains=filter_val) | Q(fireWall__model__icontains=filter_val) | Q(fireWall__version__icontains=filter_val) | Q(fireWall__sn__icontains=filter_val) | Q(action__icontains=filter_val) |\
            Q(name_phone__delivery_person__icontains=filter_val) | Q(delivery_to_category__icontains=filter_val) | Q(status__status__icontains=filter_val)
        ).order_by('-created_date')
        return new_context

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter', '')
        return context
"""
@login_required
def available(request):

    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(fireWall__vendor__icontains=query) | Q(fireWall__brand__icontains=query) | Q(fireWall__model__icontains=query) | Q(fireWall__version__icontains=query) | Q(fireWall__sn__icontains=query) | Q(replace__icontains=query) | Q(action__icontains=query) | Q(replace__icontains=query) | Q(action__icontains=query)
            results= models.Available.objects.filter(lookups).distinct()
            context={'results': results,
                     'submitbutton': submitbutton}
            return render(request, 'app/available.html', context)

        else:
            return render(request, 'app/available.html')

    else:
        return render(request, 'app/available.html')

@login_required
def received(request):

    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups=  Q(fireWall__vendor__icontains=query) | Q(fireWall__brand__icontains=query) | Q(fireWall__model__icontains=query) | Q(fireWall__version__icontains=query) | Q(fireWall__sn__icontains=query) | Q(received_from_category__icontains=query) |\
                      Q(fibr_port_num__icontains=query) | Q(eth_port_num__icontains=query) | Q(device_bog__device_bog__icontains=query) | Q(devilery_person_name__delivery_person__icontains=query) | Q(received_person_name__recieved_person__icontains=query) | Q(company__icontains=query) |\
                      Q(delivery_row__icontains=query) |  Q(status__status__icontains=query)
            results= models.Received.objects.filter(lookups).distinct()
            context={'results': results,
                     'submitbutton': submitbutton}
            return render(request, 'app/received.html', context)

        else:
            return render(request, 'app/received.html')

    else:
        return render(request, 'app/received.html')

@login_required
def delivery(request):

    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups=  Q(fireWall__vendor__icontains=query) | Q(fireWall__brand__icontains=query) | Q(fireWall__model__icontains=query) | Q(fireWall__version__icontains=query) | Q(fireWall__sn__icontains=query) | Q(action__icontains=query) |\
                      Q(name_phone__delivery_person__icontains=query) | Q(delivery_to_category__icontains=query) | Q(status__status__icontains=query)
            results= models.Delivery.objects.filter(lookups).distinct()
            context={'results': results,
                     'submitbutton': submitbutton}
            return render(request, 'app/delivery.html', context)

        else:
            return render(request, 'app/delivery.html')

    else:
        return render(request, 'app/delivery.html')
"""