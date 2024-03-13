
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    
    context = {
        'nama':'Ali'

    }

    return render(request,'index.html',context)
    #return HttpResponse('<h1>Selamat datang</h1>')

def home(request):
    return HttpResponse('<h1>Home</h1>')

def hubungi_kami(request):
    return HttpResponse('<h1>Ini Halaman Hubungi kami</h1>')