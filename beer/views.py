from django.shortcuts import render



api =  {'forms' : {},'persons': {},'newPersonId':3}
api['persons']['give']=[{'name':'Martine','beers':2, 'id':'1'}]
api['persons']['get']=[{'name':'Kevin','beers':3, 'id':'2'}]


def home(request):
  import requests
  api['api']=request.POST
  if request.method == "POST":
    if 'add' in request.POST:
      api['persons'][request.POST['add']].append({'name':request.POST['name'], 'beers':0, 'id':str(api['newPersonId'])})
      api['newPersonId']+=1
    if 'more' in request.POST:
      for person in api['persons']['give']+api['persons']['get']:
        if person['id']==request.POST['more']:
          person['beers']+=1
    if 'less' in request.POST:
      for person in api['persons']['give']+api['persons']['get']:
        if person['id']==request.POST['less'] and person['beers']>0:
          person['beers']-=1
    if 'delete' in request.POST:
      for person in api['persons']['give']:
        if person['id']==request.POST['delete']:
          api['persons']['give'].remove(person)
      for person in api['persons']['get']:
        if person['id']==request.POST['delete']:
          api['persons']['get'].remove(person)
 
  return render(request, 'home.html', {'api' : api})

def create(request):
  return render(request, 'create.html', {'api' : request.POST['add']})

def login(request):
  return render(request, 'login.html', {'api' : api})


def about(request):
    return render(request, 'about.html', {})
