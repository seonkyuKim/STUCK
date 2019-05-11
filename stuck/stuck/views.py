from django.shortcuts import render

def index(request):
    return render(request, 'main.html')

def update_info(request):
    if request.method == 'POST':
        if 
