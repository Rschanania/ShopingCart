from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as authorize, logout as deauth
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from . models import UserProfile


def logout(request):
    if request.user.is_authenticated:
        deauth(request)
        messages.info(request, "You are succefully log out ")
        return redirect('/user/login')

    return redirect('/user/login')


def Home(request):
    if request.user.is_authenticated:
        return redirect('/user/profile')

    return render(request,'home.html')


def login(request):

    if request.method == "POST":
       # form=AuthenticationForm()
        uname = request.POST['username']
        upass = request.POST['password']
        user = authenticate(username=uname, password=upass)
        if user is None:
            messages.info(request, 'user or password is not correct')
            return redirect('/user/login')
        else:
            authorize(request, user)
            return redirect('/user/profile')
    else:
        if request.user.is_authenticated:
            return redirect('/user/profile')
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return redirect('/user/profile')
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            
            form.save()
            
            messages.add_message(request, messages.INFO,
                                 "user successfully created ")
            
            return redirect('/user/login/')

    return render(request, 'register.html', {'form': form})


def profile(request):
    if request.user.is_authenticated:
        user=User.objects.get(username=request.user)
        print(user.id)
        #pro=UserProfile.objects.filter(user_id=user.id)
        #print(pro.phone
        user_pro=user.userprofile
        
        return render(request, 'profile.html',{'user':user,'pro':user_pro})
    else:
        messages.info(request, 'YOu are not loged in ')
        return redirect('/user/login')


def updateProfile(request):
    if request.method=='POST' and request.user.is_authenticated:
        print("hello")
        print(request.POST)
        u = request.user
        print(u)
        # username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        user=User.objects.get(username=u)
        phone=request.POST['phone']
        
        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        user.save()

        user = request.user

        #.update(user_id=user.id,phone=phone,image=image)
        if (UserProfile.objects.filter(user_id=user.id).count()>0):
            User_Data=UserProfile.objects.get(user_id=user.id)
            User_Data.phone=phone
            
            User_Data.save()
        else:
            UserProfile.objects.create(user_id=user.id,phone=phone)

        

        
        #user.update(first_name=first_name,last_name=last_name,email=email)
        
        data = {'user': user}
        return render(request, 'update_Profile.html', data)
    elif request.user.is_authenticated:
        u = request.user
        print(request)
        messages.info(request, 'YOu are not loged in ')
        return render(request,'update_Profile.html')
    else:
        return redirect('/user/login')