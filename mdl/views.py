from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def stud_view (request):
    msg ="<h1> first msg </h1>"
    return HttpResponse(msg)