from django.shortcuts import render,redirect
from django .urls import path
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from . forms import CategoryForm,ProductForm,ProfileForm



@login_required(login_url='login/')
def home(request):
    x=Products.objects.all()
    caty=Categories.objects.all()
    return render(request, "myApp/home.html",{'abc':x,'cat':caty})

def viewfn(request,prod_id):
    detail=Products.objects.get(id=prod_id)
    return render(request, "myApp/view.html",{"d":detail})

def categorypage(request,c_id):
    categories=Products.objects.filter(category=c_id)
    caty=Categories.objects.all()
    return render(request,"myApp/categories.html",{'cat':categories,'c':caty})
def Formfn(request):

    return render(request,"myApp/register.html")

def Resultfn(request):
    x=request.GET['num1']
    y=request.GET['num2']
    c=int(x)+int(y)
    return render(request,"myApp/resultpage.html",{"r":c})

def regfn(request):
    if request.method == "POST":
        user_name= request.POST['user_name']
        em=request.POST['email']
        firstname=request.POST['first_name']
        lastname=request.POST['second_name']
        password1=request.POST['password']
        password2=request.POST['confirm_password']
        if  password1==password2:

            if User.objects.filter(username=user_name).exists():
                messages.error(request, 'Username already exists')
                return render(request,'myApp/regfn.html')
            else:

               
                User.objects.create_user(username=user_name,email=em,first_name=firstname,last_name=lastname,password=password2)
                
                return redirect('/')
        else:
            return render(request, 'myApp/regfn.html',{'user1' :user_name})
    else:
        return render(request,'myApp/regfn.html')


def Logfn(request):
    if request.method == "POST":
        user_name= request.POST['user_name']
        password=request.POST['password']

        us=auth.authenticate(username=user_name,password=password)
        if  us:
            auth.login(request,us)
            return redirect('/')

        else:
            messages.error(request,"invalid credentials..")
            return redirect('/login/')
    else:
        return render(request,'myApp/login.html')

def logoutfn(request):
    auth.logout(request)
    return redirect('/login/')

def addCategory(request):

    if request.method == "POST":
        form=CategoryForm(request.POST, request.FILES)
        if  form.is_valid():
            form.save()
            return redirect('/')
    else:    
        f=CategoryForm()
        return render (request, 'myApp/addcat.html',{'form':f})


@login_required(login_url='/login')
def addProduct(request):
    if request.method == "POST":
        form=ProductForm(request.POST, request.FILES)
        if  form.is_valid():
            x=form.save(commite=False)
            x.us=request.user
            x.save()
            return redirect('/')
    else:    
        f=ProductForm()
        return render (request, 'myApp/addcat.html',{'form':f})


@login_required(login_url='/login')
def editProduct(request,p_id):
    if request.method == "POST":
        a=Products.objects.get(id=p_id)
        form=ProductForm(request.POST, request.FILES)
        if  form.is_valid():
            form.save()
            return redirect('/')
    else:   
        a=Products.objects.get(id=p_id)
        f=ProductForm(instance=a)
        return render (request, 'myApp/addcat.html',{'form':f})    

def deleteProduct(request,p_id):
    if request.method == "POST":
        a=Products.objects.get(id=p_id)
        form=ProductForm(request.POST, request.FILES)
        a.delete
        return redirect('/')
        

@login_required(login_url='/login')

def addProfile(request):
    if request.method == "POST":
        form=ProfileForm(request.POST, request.FILES)
        if  form.is_valid():
            x=form.save(commite=False)
            x.us=request.user
            x.save()
            return redirect('/')
    else:    
        f=ProfileForm()
        return render (request, 'myApp/addprofile.html',{'form':f})
    

def profile(request):
    x=Products.objects.filter(us=request.user.id)
    
    return render(request, "myApp/profilepage.html",{'abc':x})    
  