from django.shortcuts import render,HttpResponse

# Create your views here.
def signin(request):
    return render(request, 'signin.html'),