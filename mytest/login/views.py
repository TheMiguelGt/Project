from django.shortcuts import render

# Create your views here.
def choose(request):
    return render(request, 'choose.html')

def teach(request):
    return render(request, 'teach.html')

def student(request):
    return render(request, 'student.html')

def familiar(request):
    return render(request, 'familiar.html')