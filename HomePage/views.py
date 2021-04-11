from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {'index_active': 'active'}
    return render(request, 'Homepage/index.html', context)

def about(request):
    context = {'about_active': 'active'}
    return render(request, 'Homepage/about.html', context)

def contact(request):
    context = {'contact_active': 'active'}
    return render(request, 'Homepage/contact.html', context)