from django.http import HttpResponse
from django.shortcuts import render ,redirect
from .models import Emp
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.db import IntegrityError
from django.urls import reverse
def home(request):
   
    emps = Emp.objects.all()
    return render(request,"home.html",{
   "emps": emps
    })

def about(request):
    return render(request,"about.html",{})
       

def add(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        emp_id  = request.POST.get("emp_id")
        # phone = request.POST.get("phone")
        # address = request.POST.get("address")
        working = request.POST.get("working")
        department = request.POST.get("department")
        pic = request.FILES.get("image_image")

        print("hey",pic)
        # pic = request.POST.get("pic")
        e = Emp()
        e.name = name
        e.emp_id = emp_id
        # e.phone = phone
        # e.address = address
        e.working = working
        e.pic = pic
        e.department = department
        # e.pic= pic
        if working is None:
            e.working = False
        else:
            e.working = True   
        e.save()
        return redirect("/blog/home")
    return render(request,"add.html",{})
    
def deleteEmp(request,emp_id):
    print(emp_id)
    Emp.objects.get(id = emp_id).delete()
    return redirect("/blog/home")

def updateEmpPage(request,emp_id):
    emp = Emp.objects.get(id = emp_id)
    return render(request,"update.html",{
        "emp":emp
    })
def updateEmp(request,emp_id):
     if request.method == 'POST':
        name = request.POST.get("name")
        emp_id_a = request.POST.get("emp_id")
        # phone = request.POST.get("phone")
        # address = request.POST.get("address")
        working = request.POST.get("working")
        department = request.POST.get("department")
        pic = request.FILES.get("image_image")
        print(pic)
        e = Emp.objects.get(id=emp_id)
        e.name = name
        e.emp_id = emp_id_a
        # e.phone = phone
        # e.address = address
        e.working = working
        e.department = department
        e.pic = pic
        if working is None:
            e.working = False
        else:
            e.working = True   
        e.save()
        return redirect("/blog/home")


def Search(request):
    if request.method == 'GET':
        qu = request.GET.get('q')
        print(qu)
        if qu:
            emps = Emp.objects.filter(name =qu)
        else:
            emps = Emp.objects.all()
        return render(request,'home.html', {'emps': emps})

def login_Page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "No user with this email exists.")
            return render(request, "login.html", {})

        user = authenticate(request, username=user.username, password=password)
        if user is None:
            messages.error(request, "Invalid email or password.")
            return render(request, "login.html", {})
        else:
            login(request, user)
            return redirect("/blog/add/")

    return render(request, "login.html", {})





def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(email)
        
        # Check if email and password are provided
        if not email or not password:
            messages.error(request, "Email and password are required.")
            return redirect("/blog/home")

        try:
            # Create user object
            user = User.objects.create(
                username=email,  # User model requires a username field, so we use email as username
                email=email,
                password=password
            )

            user.set_password(password)
            user.save()
            return redirect("/blog/login/")
        
        except IntegrityError:
            messages.error(request, "A user with that email already exists.")
            return render(request, "register.html")
        
        except Exception as e:
            # Catch any other exceptions and display a generic error message
            messages.error(request, "An error occurred during registration. Please try again.")
            return render(request, "register.html")

    return render(request, "register.html", {})

def logout_Page(request):
    logout(request)
    return redirect("/blog/home/")
