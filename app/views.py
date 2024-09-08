from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View
from django.contrib import messages
from app.models import User,Diary_Model
from app.forms import Signin_Modelform,Login_Modelfrom,Diary_Modelform
from django.utils.decorators import method_decorator

# Create your views here.

def Login_Dec(fn):
    def wrapper(request,**kwargs):
        if not request.user.is_authenticated:
            return redirect ('log')
        else:
            return fn(request,**kwargs)
    return wrapper

def Edit_Dec(fn):
    def wrapper(request,**kwargs):
        id=kwargs.get('pk')
        form=Diary_Model.objects.get(id=id)
        if form.user!=request.user:
            return redirect('log')
        else:
            return fn(request,**kwargs)
    return wrapper


class Diary_Home_View(View):
    def get(self,request,**kwargs):

        return render(request,'index.html')
    
    def post(self,request,**kwargs):

        messages.success(request,' ')
        return render(request,'index.html')
    
class Signin_view(View):
    def get(self,request,**kwargs):
        form=Signin_Modelform()
        return render(request,'signin.html',{'form':form})
    
    def post(self,request,**kwargs):
        form=Signin_Modelform(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
        return redirect('log')
        
class Login_View(View):
    def get(self,request,**kwargs):
        form=Login_Modelfrom()
        return render(request,'login.html',{'form':form})
    
    def post(self,request,**kwargs):
        form=Login_Modelfrom(request.POST)
        if form.is_valid():
            user=form.cleaned_data.get('username')
            psw=form.cleaned_data.get('password')
            data=authenticate(username=user,password=psw)
            if data:
                login(request,data)
                return redirect('diary')
            else:
                form=Login_Modelfrom()
                messages.success(request," Incorrect ' Username ' or ' Password '..........! Please try again..")
                return render(request,'login.html',{'form':form})


@method_decorator(Login_Dec,name='dispatch')
class Logout_View(View):
    def get(self,request):
        logout(request)
        messages.success(request,"Successfully Logged Out")
        return redirect('home')
    

@method_decorator(Login_Dec,name='dispatch')
class Diary_view(View):
    def get(self,request,**kwargs):
        form=Diary_Modelform()
        return render(request,'diary.html',{'form':form})
    
    def post(self,request,**kwargs):
        form=Diary_Modelform(request.POST)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
        form=Diary_Modelform()
        return render(request,'diary.html',{'form':form})
    
@method_decorator(Login_Dec,name='dispatch')
class All_View(View):
    def get(self,request,**kwargs):
        form=Diary_Model.objects.filter(user=request.user)
        return render(request,'all.html',{'form':form})
    

@method_decorator(Login_Dec,name='dispatch')
@method_decorator(Edit_Dec,name='dispatch')
class Update_Diary_View(View):
    def get(self,request,**kwargs):
        id=kwargs.get('pk')
        data=Diary_Model.objects.get(id=id)
        form=Diary_Modelform(instance=data)
        return render(request,'update.html',{'form':form})
    
    def post(self,request,**kwargs):
        id=kwargs.get('pk')
        data=Diary_Model.objects.get(id=id)
        form=Diary_Modelform(request.POST,instance=data)
        if form.is_valid():
            form.save()
        return redirect('all')

@method_decorator(Login_Dec,name='dispatch')  
@method_decorator(Edit_Dec,name='dispatch')
class Read_View(View):
    def get(self,request,**kwargs):
        id=kwargs.get('pk')
        data=Diary_Model.objects.get(id=id)
        form=Diary_Modelform(instance=data)
        return render(request,'read.html',{'form':form})


@method_decorator(Login_Dec,name='dispatch')  
@method_decorator(Edit_Dec,name='dispatch')
class Delete_Diary_View(View):
    def get(self,request,**kwargs):
        id=kwargs.get('pk')
        data=Diary_Model.objects.get(id=id)
        form=Diary_Modelform(instance=data)
        messages.success(request,"Are you sure you want to delete this diary ..?")
        return render(request,'delete.html',{'form':form})
    
    def post(self,request,**kwargs):
        id=kwargs.get('pk')
        Diary_Model.objects.get(id=id).delete()
        return redirect('all')




