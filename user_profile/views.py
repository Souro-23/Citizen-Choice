from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Profile

# Create your views here.


def Signup(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username= form.cleaned_data.get('username')
			messages.success(request,f'Acount created for {username}!')
			return redirect('login')
	else:
		form= UserRegisterForm()
	return render(request,'HomePage/signup.html',{'form':form})



def createProfile(request):
	p=Profile(user=request.user,slug=request.user.username)
	p.save()
	return redirect('home')
