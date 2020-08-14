from django.http import HttpResponse
from datetime import datetime


# Function view
def welcome(request):
    return HttpResponse("<h1 style='color:blue'>Welcome to Django!</h1>")


def wish(request):
    ct = datetime.now()
    if ct.hour < 12:
        msg = "Good Morning"
    elif ct.hour < 17:
        msg = "Good Afternoon"
    else:
        msg = "Good Evening"

    if 'name' in request.GET:
        name = request.GET['name']
    else:
        name = "Guest"
    return HttpResponse(f"<h1 style='color:green'>{msg} {name}</h1>")
