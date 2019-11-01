from django.shortcuts import render

def home(request):
  import json
  import requests

  if request.method == "POST":
    zipcode = request.POST['zipcode']
   
    return render(request, 'home.html', {'api' : 'toto'})
 
  return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})
