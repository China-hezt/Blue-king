# -*- coding: utf-8 -*-

from common.mymako import render_mako_context
from blueking.component.shortcuts import get_client_by_request
from django.db.models import Q
from .models import Bookcar

def home(request):
    return render_mako_context(request, '/home_application/home.html')

def index(request):
    return render_mako_context(request, '/autocar/index.html')

def table(request):
    lists = Bookcar.objects.all()

    print lists
    for list in lists:
        print list.Brand
        print list.Model
        print list.Year
        print list.Type
        print list.Cooler
    countext = {'lists': lists}
    return render_mako_context(request, '/autocar/table.html', countext)

def table_1(request):
    Brand_filder = request.GET.get('Brand')
    Model_filder = request.GET.get('Model')
    Year_filder = request.GET.get('Year')

    lists = Bookcar.objects.filter(Q(Brand=Brand_filder) | Q(Model=Model_filder) | Q(Year=Year_filder))
    countext = {'lists': lists}
    return render_mako_context(request, '/autocar/table.html', countext)

def table1(request):
    lists = Bookcar.objects.all()
    for list in lists:
        print list.Brand
        print list.Model
        print list.Year
        print list.Type
        print list.Cooler
    countext = {'lists': lists}
    return render_mako_context(request, '/autocar/table1.html', countext)

def table1_1(request):
    Brand_filder = request.GET.get('Brand')
    Model_filder = request.GET.get('Model')
    Year_filder = request.GET.get('Year')

    lists = Bookcar.objects.filter(Q(Brand=Brand_filder) | Q(Model=Model_filder) | Q(Year=Year_filder))
    countext = {'lists': lists}
    return render_mako_context(request, '/autocar/table1.html', countext)


def table2(request):
    return render_mako_context(request, '/autocar/table2.html')
