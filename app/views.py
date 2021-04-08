from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.views import generic
from rest_framework import generics, serializers, filters
from django.db.models import Q



def index(request):
    return render(request, 'app/index.html')


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
