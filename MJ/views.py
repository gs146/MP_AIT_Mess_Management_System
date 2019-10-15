from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import report_feed
# Create your views here.
def index(request):
    return render(request, 'index.html')


def feedback(request):
    if request.method == 'POST':
        name1 = request.POST.get('name')
        reg_no = request.POST.get('regno')
        message = request.POST.get('message')
        print(name1)

        f = report_feed(user_name = name1, reg_no= reg_no, message = message)
        f.save()
        return redirect( '/mj')
    else:
         
        return render(request, 'feedback.html')



def menu(request):
    return render(request, 'menu.html')