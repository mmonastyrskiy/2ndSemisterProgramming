from django.shortcuts import render
from django.http import Http404,HttpResponse
from models import Goods

def Goods(request,id):
	return HttpResponse(f"Открыта страница {id}")



# Create your views here.
