import xlwt
from datetime import datetime

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse

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


class ExportView(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename='\
            + 'Export_{}.csv'.format(datetime2jalali(datetime.now()).strftime('%Y/%m/%d-%H:%M:%S'))

        wb = xlwt.Workbook(encoding='utf-8')

        # START Received From Category
        ws = wb.add_sheet('Received From Category')
        # Sheet header
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns = [
            "ID",
            "Firewall Vendor",
            "Firewall Brand",
            "Firewall Model",
            "Firewall FW",
            "Firewall Serial Number",
            "Firewall Fiber Port Number",
            "Firewall Ethernet Port Number",
            "Category",
            "Device Problem",
            "Received Person Name",
            "Received Person Phone",
            "Category Person Name",
            "Category Person Phone",
            "Date/Time",
            "Status",
            "Description",
        ]
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)
        # Sheet body
        font_style = xlwt.XFStyle()
        # make data list
        rows_data = []
        received_from_category = ReceivedFromCategory.objects.all().order_by("-date")
        for obj in received_from_category:
            row_data = []
            row_data.append(obj.id)
            if obj.firewall is not None:
                row_data.extend(
                    [
                        obj.firewall.vendor,
                        obj.firewall.brand,
                        obj.firewall.model,
                        obj.firewall.version,
                        obj.firewall.sn,
                        obj.firewall.fiber_port_num,
                        obj.firewall.eth_port_num,
                    ]
                )
            else:
                row_data.extend(
                    [
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                    ]   
                )
            if obj.category is not None:
                row_data.extend(
                    [obj.category.name,]
                )
            else:
                row_data.extend(
                    ["",]
                )
            if obj.device_problem is not None:
                row_data.extend(
                    [obj.device_problem.name,]
                )
            else:
                row_data.extend(
                    ["",]
                )
            if obj.received_person is not None:
                row_data.extend(
                    [
                        obj.received_person.name,
                        obj.received_person.phone_number,
                    ]
                )
            else:
                row_data.extend(
                    [
                        "",
                        "",
                    ]
                )
            if obj.category_person is not None:
                row_data.extend(
                    [
                        obj.category_person.name,
                        obj.category_person.phone_number,
                    ]
                )
            else:
                row_data.extend(
                    [
                    "",
                    "",
                    ]
                )
            row_data.extend(
                    [
                        datetime2jalali(obj.date).strftime('%Y/%m/%d %H:%M'),
                    ]
                )
            if obj.status is not None:
                row_data.extend(
                    [
                        obj.status.name,
                    ]
                )
            else:
                row_data.extend(
                    [
                        "",
                    ]
                )
            row_data.extend(
                    [
                        obj.description,
                    ]
                )
            rows_data.append(row_data)
        # write data to sheet
        for row in rows_data:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)
        

        # START Delivery To Company
        ws = wb.add_sheet('Delivery To Company')
        # Sheet header
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns = [
            "ID",
            "Firewall Vendor",
            "Firewall Brand",
            "Firewall Model",
            "Firewall FW",
            "Firewall Serial Number",
            "Firewall Fiber Port Number",
            "Firewall Ethernet Port Number",
            "Action",
            "Date/Time",
            "Delivery Person Name",
            "Delivery Person Phone",
            "Company Person Name",
            "Company Person Phone",
            "Status",
            "Description",
        ]
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)
        # Sheet body
        font_style = xlwt.XFStyle()
        # make data list
        rows_data = []
        delivery_to_company = DeliveryToCompany.objects.all().order_by("-date")
        for obj in delivery_to_company:
            row_data = []
            row_data.append(obj.id)
            if obj.firewall is not None:
                row_data.extend(
                    [
                        obj.firewall.vendor,
                        obj.firewall.brand,
                        obj.firewall.model,
                        obj.firewall.version,
                        obj.firewall.sn,
                        obj.firewall.fiber_port_num,
                        obj.firewall.eth_port_num,
                    ]
                )
            else:
                row_data.extend(
                    [
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                    ]   
                )
            row_data.append(obj.action)
            row_data.append(datetime2jalali(obj.date).strftime('%Y/%m/%d %H:%M'))
            if obj.delivery_person is not None:
                row_data.extend(
                    [
                        obj.delivery_person.name,
                        obj.delivery_person.phone_number,
                    ]
                )
            else:
                row_data.extend(
                    [
                        "",
                        "",
                    ]
                )
            if obj.company_person is not None:
                row_data.extend(
                    [
                        obj.company_person.name,
                        obj.company_person.phone_number,
                    ]
                )
            else:
                row_data.extend(
                    [
                    "",
                    "",
                    ]
                )
            if obj.status is not None:
                row_data.extend(
                    [
                        obj.status.name,
                    ]
                )
            else:
                row_data.extend(
                    [
                        "",
                    ]
                )
            row_data.extend(
                    [
                        obj.description,
                    ]
                )
            rows_data.append(row_data)
        # write data to sheet
        for row in rows_data:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        
        # START Received From Company
        ws = wb.add_sheet('Received From Company')
        # Sheet header
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns = [
            "ID",
            "Firewall Vendor",
            "Firewall Brand",
            "Firewall Model",
            "Firewall FW",
            "Firewall Serial Number",
            "Firewall Fiber Port Number",
            "Firewall Ethernet Port Number",
            "Old Firewall Vendor",
            "Old Firewall Brand",
            "Old Firewall Model",
            "Old Firewall FW",
            "Old Firewall Serial Number",
            "Old Firewall Fiber Port Number",
            "Old Firewall Ethernet Port Number",
            "Company",
            "Device Problem",
            "Company Person Name",
            "Company Person Phone",
            "Received Person Name",
            "Received Person Phone",
            "Date/Time",
            "Status",
            "Description",
        ]
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)
        # Sheet body
        font_style = xlwt.XFStyle()
        # make data list
        rows_data = []
        received_from_company = ReceivedFromCompany.objects.all().order_by("-date")
        for obj in received_from_company:
            row_data = []
            row_data.append(obj.id)
            if obj.firewall is not None:
                row_data.extend(
                    [
                        obj.firewall.vendor,
                        obj.firewall.brand,
                        obj.firewall.model,
                        obj.firewall.version,
                        obj.firewall.sn,
                        obj.firewall.fiber_port_num,
                        obj.firewall.eth_port_num,
                    ]
                )
            else:
                row_data.extend(
                    [
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                    ]   
                )
            if obj.firewall_changes is not None:
                if obj.firewall_changes.old_firewall is not None:
                    row_data.extend(
                        [
                            obj.firewall_changes.old_firewall.vendor,
                            obj.firewall_changes.old_firewall.brand,
                            obj.firewall_changes.old_firewall.model,
                            obj.firewall_changes.old_firewall.version,
                            obj.firewall_changes.old_firewall.sn,
                            obj.firewall_changes.old_firewall.fiber_port_num,
                            obj.firewall_changes.old_firewall.eth_port_num,
                        ]
                    )
                else:
                    row_data.extend(
                        [
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                            "",
                        ]   
                    )
            else:
                row_data.extend(
                    [
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                    ]   
                )
            if obj.company is not None:
                row_data.extend(
                    [
                        obj.company.name,
                    ]
                )
            else:
                row_data.extend(
                    [
                        "",
                    ]
                )
            if obj.device_problem is not None:
                row_data.extend(
                    [
                        obj.device_problem.name,
                    ]
                )
            else:
                row_data.extend(
                    [
                        "",
                    ]
                )
            if obj.company_person is not None:
                row_data.extend(
                    [
                        obj.company_person.name,
                        obj.company_person.phone_number,
                    ]
                )
            else:
                row_data.extend(
                    [
                        "",
                    ]
                )
            if obj.received_person is not None:
                row_data.extend(
                    [
                        obj.received_person.name,
                        obj.received_person.phone_number,
                    ]
                )
            else:
                row_data.extend(
                    [
                        "",
                        "",
                    ]
                )
            row_data.append(datetime2jalali(obj.date).strftime('%Y/%m/%d %H:%M'))
            if obj.status is not None:
                row_data.extend(
                    [
                        obj.status.name,
                    ]
                )
            else:
                row_data.extend(
                    [
                        "",
                    ]
                )
            row_data.extend(
                    [
                        obj.description,
                    ]
                )
            rows_data.append(row_data)
        # write data to sheet
        for row in rows_data:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        
        # START Delivery To Category
        ws = wb.add_sheet('Delivery To Category')
        # Sheet header
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns = [
            "ID",
            "Firewall Vendor",
            "Firewall Brand",
            "Firewall Model",
            "Firewall FW",
            "Firewall Serial Number",
            "Firewall Fiber Port Number",
            "Firewall Ethernet Port Number",
            "Action",
            "Date/Time",
            "Delivery Person Name",
            "Delivery Person Phone",
            "Category Person Name",
            "Category Person Phone",
            "Category",
            "Status",
            "Description",
        ]
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)
        # Sheet body
        font_style = xlwt.XFStyle()
        # make data list
        rows_data = []
        delivery_to_category = DeliveryToCategory.objects.all().order_by("-date")
        for obj in delivery_to_category:
            row_data = []
            row_data.append(obj.id)
            if obj.firewall is not None:
                row_data.extend(
                    [
                        obj.firewall.vendor,
                        obj.firewall.brand,
                        obj.firewall.model,
                        obj.firewall.version,
                        obj.firewall.sn,
                        obj.firewall.fiber_port_num,
                        obj.firewall.eth_port_num,
                    ]
                )
            else:
                row_data.extend(
                    [
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                    ]   
                )
            row_data.append(obj.action)
            row_data.append(datetime2jalali(obj.date).strftime('%Y/%m/%d %H:%M'))
            if obj.delivery_person is not None:
                row_data.extend(
                    [
                        obj.delivery_person.name,
                        obj.delivery_person.phone_number,
                    ]
                )
            else:
                row_data.extend(
                    [
                        "",
                    ]
                )
            if obj.category_person is not None:
                row_data.extend(
                    [
                        obj.category_person.name,
                        obj.category_person.phone_number,
                    ]
                )
            else:
                row_data.extend(
                    [
                        "",
                        "",
                    ]
                )
            if obj.category is not None:
                row_data.extend(
                    [
                        obj.category.name,
                    ]
                )
            else:
                row_data.extend(
                    [
                        "",
                    ]
                )
            if obj.status is not None:
                row_data.extend(
                    [
                        obj.status.name,
                    ]
                )
            else:
                row_data.extend(
                    [
                        "",
                    ]
                )
            row_data.extend(
                    [
                        obj.description,
                    ]
                )
            rows_data.append(row_data)
        # write data to sheet
        for row in rows_data:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)
        return response