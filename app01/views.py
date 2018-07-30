from django.shortcuts import render

# Create your views here.

def app01(request):
    return render(request,'master/master.html')