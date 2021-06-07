from django.http import HttpResponse
from django.shortcuts import render,redirect


# def home_page(request):
#     return HttpResponse("Welcome to Recruitment_information_recommendation_platform ! ")

def home_page(request):
    if request.session.get('is_login', None):
        return redirect('/user/login/')
    return render(request, 'index.html')
