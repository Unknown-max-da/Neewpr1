from django.shortcuts import render
from .models import Person
from django.http import Http404
# Create your views here.

def personn(request):
    persons=Person.objects.all()
    context={'persons':persons}
    return render(request,'odamlar.html',context)

def personn_detail(request,id):
    try:
        person=Person.object.get(id=id)
        context={'person':person}
    except:
        raise Http404("Page not found!")
    return render(request, 'pers_det.html', context)