from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def mycv(request):
    if request.method=="POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("mycv")
        
    context ={}

    # add the dictionary during initialization
    context["cv"] = Berita.objects.all()
    context["rev"] = Review.objects.all()
    return render(request, "MyCV.html", context)