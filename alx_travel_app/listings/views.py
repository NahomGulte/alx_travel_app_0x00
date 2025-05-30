from django.shortcuts import render

from django.http import HttpResponse

def Welcome(request):
    return HttpResponse("Hello welcome to our Apartment Listing website where we post apaerments all over the City of Addis Ababa that are available for a rent or also for a purchase")
