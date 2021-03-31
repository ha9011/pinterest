from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    qwe = "q"
    #return HttpResponse("hello world!")
    return render(request, "account/hello_world.html")  # templates in setting 설정