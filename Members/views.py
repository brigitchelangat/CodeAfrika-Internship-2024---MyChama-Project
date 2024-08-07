from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Member 

# Display a list of all students

def member_list(request):
    members = Member.objects.all()
    return render(request, 'member/list.html',{'members':members})


# Display a single student

def member_details(request,id):
    member = Member.objects.get(id=id)

    return render(request, 'member/detail.html',{'member':member})
    