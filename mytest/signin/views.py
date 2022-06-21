from django.shortcuts import render,HttpResponse

# Create your views here.
def signin(request):
    return render(request, 'choose.html')

def teach(request):
    return render(request, 'teach.html')

def student(request):
    return render(request, 'student.html')

def familiar(request):
    return render(request, 'familiar.html')