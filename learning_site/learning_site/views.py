from django.shortcuts import render

def home(request):
    return render(
        request,
        'home.html' # doesnt live in any directory
    )