from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["buku"] = Buku.objects.all()
    return render(request, "homepage.html", context)

def detail_view(request, id):
    print(request.get_full_path())
    context ={}

    # add the dictionary during initialization
    context["data"] = Buku.objects.get(ID_Buku = id)
    context["terbit"] = Penerbit.objects.filter(ID_Penerbit = id)
    return render(request, "homepage.html", context)