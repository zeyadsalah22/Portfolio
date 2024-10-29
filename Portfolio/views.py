from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import Certificate,Project,Texter
import json 
def index(request):
    
    certificates = Certificate.objects.all().order_by('order')
    webs = Project.objects.filter(category='Web Development').order_by('order')
    ais = Project.objects.filter(category='AI').order_by('order')
    digitals = Project.objects.filter(category='Digital Marketing').order_by('order')
    
    return render(request, 'portfolio/index.html', {
        'certificates': certificates,
        'webs': webs,
        'ais': ais,
        'digitals': digitals,
    })


def certificate(request):
    certificates = Certificate.objects.all().order_by('order')
    return render(request,'portfolio/certificate.html',{
        'certificates' : certificates
    })

def contact(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data['name']
        message = data['message']
        email = data['email']
        new_text = Texter(name=name,email=email,message=message)
        new_text.save()
        return JsonResponse({"message": "message sent successfully."}, status=201)

    else:
        return render(request,'portfolio/contact.html')

def projects(request):
    webs = Project.objects.filter(category='Web Development').order_by('order')
    ais = Project.objects.filter(category='AI').order_by('order')
    digitals = Project.objects.filter(category='Digital Marketing').order_by('order')
    return render(request,'portfolio/projects.html',{
        'webs': webs,
        'ais': ais,
        'digitals': digitals
    })


def about(request):
    return render(request,'portfolio/about.html')