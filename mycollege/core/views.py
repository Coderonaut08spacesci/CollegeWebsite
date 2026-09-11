from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def principal_message(request):
    return render(request, 'core/principal_message.html')

def courses(request):
    return render(request, 'core/courses.html')

def syllabus(request):
    return render(request, 'core/syllabus.html')

def fees(request):
    return render(request, 'core/fees.html')

def admission(request):
    return render(request, 'core/admission.html')