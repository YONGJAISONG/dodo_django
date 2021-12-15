from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import members

def index(request):
    member = members.objects.all()

    return render(
        request,
        'members/index.html',
        {
            'member' : member,
        }
    )