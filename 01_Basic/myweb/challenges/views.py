from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
months = list(challenges.keys())


def index(request):
    list_items = ""

    for month in months:
        # Creating puerly dynamic url
        month_path = reverse("month-name", args=[month])
        list_items += f"<li><a href='{month_path}'>{month.capitalize()}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


# Create your views here.
# Creating first function based view
# def index(request):

#     return HttpResponse("Learn coding 30 minutes each day.")

# Creating a generic few for all the months

def monthly_challenge(request, month):
    

    try:
       
        response_data = f"<h1>{challenges[month]}</h1>"
        return HttpResponse(response_data)

    except:
        return HttpResponseNotFound("This url is not supported.\n Please check your url. ")
