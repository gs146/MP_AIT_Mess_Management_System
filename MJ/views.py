from django.shortcuts import render
from django.http import HttpResponse

from .models import feedback
# Create your views here.
def index(request):
    return render(request, 'index.html')


def feedback(request):
    name1 = request.POST.get('name')
    reg_no = request.POST.get('regno')
    message = request.POST.get('message')

    f = feedback(name = name1, reg_no= reg_no, message = message)
    f.save()
    return render(request, 'feedback.html')



def menu(request):
    return render(request, 'menu.html')