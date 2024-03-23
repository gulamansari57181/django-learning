from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

challenges = {
    "january": "Learn coding 30 minutes each day.",
    "febuary": "Walk for at least 20 minutes every day.",
    "march": "Drink 4L of water each day.",
    "april": "Take no coffe in the entire month.",
    "may": "Eat no meat in the complete month.",
    "june": "Learn React Web framework.",
    "july": "Teach student about hoe to handle exam pressure.",
    "august": "Read at least 3 books in the month.",
    "september": "Do excersise in alternate days.",
    "october": "Learn to type faster by taking professional typing course.",
    "november": "Don't drink carbonated soft drinks and packages food.",
    "december": "Donate 15% of my salary to needy people.",

}


# Create your views here.
# Creating first function based view
# def index(request):

#     return HttpResponse("Learn coding 30 minutes each day.")

# Creating a generic few for all the months

def monthly_challenge(request, month):
    
    try:
        return HttpResponse(challenges[month])

    except:
        return HttpResponseNotFound("This url is not supported.\n Please check your url. ")

    
