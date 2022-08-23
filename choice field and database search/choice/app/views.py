from curses import KEY_A1, has_ic
from logging import LoggerAdapter, logThreads
from django.shortcuts import render
from django.db.models import Q

from . models import Car, student
from . forms import GeeksForm
# Create your views here.




def home_view(request):
    context = {}
    context['form'] = GeeksForm()
    return render( request, "home.html", context)


def choice(request):
    if request.method=='POST':
        name=request.POST['cars']
        print(name)
        stu = Car.objects.create(Car_name=name)
        stu.save()
    return render(request,"choice.html")


def show(request):
    getstudent = None

    if request.GET.get("qs"):
        getstudent = student.objects.filter(
            Q(first_name__contains = request.GET.get("qs")) | 
            Q(last_name__contains = request.GET.get("qs"))  |
            Q(stream__contains = request.GET.get("qs"))   
            )
    context = {
        "students":getstudent
    }
    return render(request,"test.html",context)



