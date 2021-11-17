from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


#primeira view
def home(request):
    return HttpResponse('Olá django')