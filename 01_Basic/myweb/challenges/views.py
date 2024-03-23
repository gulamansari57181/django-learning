from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Creating first function based view


def index(request):

    return HttpResponse("Hurray!! This is working.")
