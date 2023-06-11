from django.http import HttpRequest
from django.shortcuts import render


# Create your views here.
def aboutme(request: HttpRequest):
    return render(request, "aboutme/aboutme.html")
