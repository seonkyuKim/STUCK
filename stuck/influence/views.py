from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index_influencer.html')



def register_info(request):
    pass
