from django.shortcuts import render
from django.http import HttpResponse

from .models import Volunteers

# Create your views here.
def index(request):
    #return HttpResponse('HELLO FROM POSTS')

    volunteers = Volunteers.objects.all()[:10]

    context = {
      'title':'Volunteers1',
      'volunteers': volunteers
    }

    return render(request,'volunteers/index.html', context)

def details(request, id):
    volunteer = Volunteers.objects.get(id=id)

    context= {
    'volunteer' : volunteer
    }

    return render(request,'volunteers/details.html', context)
