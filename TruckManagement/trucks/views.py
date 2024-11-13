from django.shortcuts import loader
from django.http import HttpResponse
from .models import Trucks


def trucks(request):
    mytrucks = Trucks.objects.all().values()
    template = loader.get_template('all_trucks.html')
    context = {
        'mytrucks':mytrucks,
    }
    return HttpResponse(template.render(context, request))
   


def info(request, engine_model):
    mytrucks = Trucks.objects.get(engine_model=engine_model)
    template = loader.get_template('details.html')
    context = {
        'mytrucks': mytrucks,
    }

    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def testing (request):
    template = loader.get_template(template.html)
    context = {
        'fruits': ['Apple', 'Banana', 'Grapes']
    }

    return HttpResponse(template.render(context, request))