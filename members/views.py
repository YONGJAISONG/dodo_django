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

def members_page(request, pk):
    member = members.objects.get(pk=pk)

    return render(
        request,
        'members/member_info.html',
        {
            'member' : member
        }
    )