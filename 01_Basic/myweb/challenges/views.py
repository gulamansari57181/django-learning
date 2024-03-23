from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
# Creating first function based view


# def index(request):

#     return HttpResponse("Learn coding 30 minutes each day.")


# # Creating a function based view for feb

# def feb(request):
    
#     return HttpResponse("Walk for at least 20 minutes every day.")


# Creating a generic few for all the months

def monthly_challenge(request,month):
    challlenge_text=None
    if month=="january":
        challlenge_text="Learn coding 30 minutes each day."
    
    elif month=="febuary":
        challlenge_text="Walk for at least 20 minutes every day."
    
    elif month=="march":
        challlenge_text="Drink 4L of water each day."
    
    else:
        return HttpResponseNotFound("This url is not supported.\n Please check your url. ")
        
    
    return HttpResponse(challlenge_text)