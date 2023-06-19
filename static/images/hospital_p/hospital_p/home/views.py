from django.shortcuts import render,redirect
from.models import Department,Docter
from django.contrib import messages
from.forms import BookingForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User,auth
# Create your views here.
def index(request):
    return render(request,'index.html')
@login_required(login_url='login')
def department(request):
    department= Department.objects.filter(status=0)
    
    return render(request,'departments.html',{"department":department})

def doctors(request,slug):
 if(Department.objects.filter(slug=slug,status=0)):
    docters=Docter.objects.filter(docter__slug=slug)
    return render(request,'doctors.html',{"docters":docters})
 else:
        messages.warning(request,"no")
        return redirect('collections')



@login_required(login_url='login')
def booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
    form = BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'book.html',dict_form)

def loginn(request):
    
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        
        else:
            messages.info(request,"invalid login")
            return redirect('login')
    else:
            # User is authenticated
       return render(request,"login.html")    
    
def logout(request):
    auth.logout(request)
    return redirect('/')    

    return render(request,'login.html')

def register(request):
    if request.method == "POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request,"username already exists")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email taken")  
            return redirect('register')
        else:  
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save();
        return redirect('/')
        
    else:
        return render(request,"register.html")
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
def about(request):
    return render(request,'about.html')