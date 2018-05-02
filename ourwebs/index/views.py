from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index_views(respect):
    return render(respect,'index.html')
