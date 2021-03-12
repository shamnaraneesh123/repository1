from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def testfun(request):
   return HttpResponse('HelloWorld') 
def test2fun(request):
    return HttpResponse('hi')
def test3fun(request):
    return render(request,'test.html')
def test4fun(request):
    return render(request,'test1.html')
