from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dashboard(request):
    return HttpResponse('<h1>ini halaman dashboard pada aplikasi akademik')