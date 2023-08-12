from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import View
from .forms import Register,logform
# Create your views here.
class signup(View):
    def get(self,request):
        f=Register(None)
        return render(request,'programe/signup.html',{"data":f})
    def post(self,request):
        f=Register(request.POST)
        if f.is_valid():
            data=f.save(commit=False)
            p=f.cleaned_data.get('password')
            data.set_password(p)
            data.save()
            return redirect('app:home')
        return render(request,'programe/signup.html',{"data":f})

class signin(View):
    def get(self,request):
        f=logform(None)
        return render(request,"programe/signin.html",{'data':f})
    def post(self,request):
        f=logform(request.POST)
        if f.is_valid():
             u=f.cleaned_data.get('username')
             p=f.cleaned_data.get('password')
             ur=authenticate(username=u,password=p)
             nxt=request.GET.get('next')
             if ur:
                 login(request,ur)
                 if nxt:
                     return redirect(nxt)
             return redirect('app:home') #home ka url load krwane ke liye return mein
        return render(request,"programe/signin.html",{'data':f})
   

def signout(request):
    logout(request)
    return redirect('app:signup')    

class Home(LoginRequiredMixin,View):
    login_url='app:signin'
    def get(self,request):
        return render(request,'programe/hello.html')
    