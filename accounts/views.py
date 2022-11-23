from django.shortcuts import render,redirect

# Create your views here.
from accounts.forms import LoginForm
from django.contrib.auth import authenticate,login,logout

def login_view(request):
    form=LoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user=authenticate(username=username,password=password)
        login(request,user)
        return redirect('/')
    
    return render(request,'accounts/form.html',{'form':form})


def logout_view(request):
    logout(request)
    return redirect('/')
