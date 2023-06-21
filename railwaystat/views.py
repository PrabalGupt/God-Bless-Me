from django.shortcuts import render, redirect
from .models import TrainStatus, UserDetails
from django.http import HttpResponse, JsonResponse
# Create your views here.
def Home(request):
    return render(request, 'Home.html')

def TrainStat(request):
    return render(request, 'TrainStatus.html')

def CheckTrainStatus(request):
    TrainName = request.POST['InputValue']
    if TrainStatus.objects.filter(TrainName=TrainName).exists():
        TrainsName = TrainStatus.objects.get(TrainName=TrainName)
        # Destination = TrainStatus.objects.get(Destination=request.Destination)
        destination=TrainsName.Destination
        return render(request, 'TrainName.html',{'TrainName': TrainName, 'Destination': destination})
    else:
        return HttpResponse('Enter correct train name')

def login(request):
    name = request.POST['Username']
    password = request.POST.get('password', False)
    if UserDetails.objects.filter(Username=name).exists():
        return HttpResponse('User already exists')
    else:
        new_user = UserDetails.objects.create(Username=name)
        new_password = UserDetails.objects.create(password=password)
        new_user.save()
        new_password.save()
    return render(request, 'login.html', {'Username': name, 'password': password})

def signup(request):
    return render(request, 'signup.html')

def checkview(request):
    usersName = request.POST.get('usersname', False)
    password = request.POST.get('pass', False)
    if UserDetails.objects.filter(Username=usersName).exists() and UserDetails.objects.filter(password=password).exists():
        return render(request, 'Home.html')
    else:
        return HttpResponse('Username does not exist')

def verify(request):
    return render(request, 'login.html')
