from django.shortcuts import render
from django.http import HttpResponse

import aeroports

# Create your views here.

AIRPORT_LIST = {
'MOW' : 'MOSCOW',
'BER' : 'BERLIN',
'LGW' : 'LONDON',
'BGM' : 'NEW YORK',
'ROM' : 'ROME',
'CNI' : 'CHANGHAI',
'ORY' : 'PARIS',
'BSB' : 'BRASILIA',
'YOW' : 'OTTAWA',
'GEN' : 'OSLO',
'WAW' : 'WARSAW'
}

def cities_list(request):
    return render(request, template_name='list_of_cities.html', context={}) 
    #return HttpResponse('<h1>some_sh1t</h1>')

def airport_city(request, airport_code):
    city = AIRPORT_LIST.get(airport_code.upper(), 'Not found')
    cont = {
    'key' : city
    }
    return render(request, template_name='aeroports.html', context=cont)

def home_page(request):
    ctxt =  AIRPORT_LIST
    return render(request, template_name='home_page.html', context=ctxt)

