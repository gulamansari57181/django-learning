from django.http import HttpResponse

def home(request):
    
    return HttpResponse("<h1>Welcome to Chai's Django Project: Home page</h1>")


def about(request):
    
    return HttpResponse("<h1>Welcome to Chai's Django Project: About page</h1>")

def contact(request):
    return HttpResponse("<h1>Welcome to Chai's Django Project: Contact page</h1>")
