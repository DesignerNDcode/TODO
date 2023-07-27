from django.shortcuts import render, redirect
from .models import todo_list
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login



def Home(request):
    list_data = todo_list.objects.filter(user_name=request.user)

    data = {"list_data": list_data}

    return render(request, "index.html", data)


def add(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        name = request.POST.get("name")
        desc = request.POST.get("desc")
        date = request.POST.get("date")
        time = request.POST.get("time")
        datetime = f"{time}/{date}"
        adding = todo_list(user_name=user_name, name=name, desc=desc, end_time=datetime, status="pending")
        adding.save()

        list_data = todo_list.objects.filter(user_name=request.user)

        data = {"list_data": list_data}

        return redirect("/", data)

    return render(request, "index.html")

def edit(request, id):
    list_data = todo_list.objects.filter(user_name=request.user)

    data = {"list_data": list_data}

    if request.method == "POST":
        name = request.POST.get("name")
        desc = request.POST.get("desc")
        time = request.POST.get("end_date")
        status = request.POST.get("status")
        
        if status is None:
             status = "pending"
            
        

        editing = todo_list(id=id, user_name=request.user, name=name, desc=desc, end_time=time, status=status)
        editing.save()

        list_data = todo_list.objects.filter(user_name=request.user)

        data = {"list_data": list_data}

        return redirect("/", data)

    return render(request, "index.html", data)

def clear(request):

    list_data = todo_list.objects.filter(user_name=request.user)
    list_data.delete()

    data = {"list_data": list_data}

    return redirect("/", data)

def delete(request, id):

    list_data = todo_list.objects.filter(id=id)
    list_data.delete()

    data = {"list_data": list_data}

    return redirect("/", data)

def login_user(request):
    if request.method == "POST":
        user = request.POST.get("user")
        password = request.POST.get("password")

        user = authenticate(request, username=user, password=password)
        if user is not None:
            login(request, user)
        return redirect("/")
    
    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        user = request.POST.get("user")
        password = request.POST.get("password")
        email = request.POST.get("email")

        user = User.objects.create_user(f"{user}", f"{email}", f"{password}")
        user.save()
        user1 = authenticate(request, username=user, password=password)
        if user1 is not None:
            login(request, user1)
        return redirect("/")
    return render(request, "index.html")


        
def logout_view(request):
    logout(request)
    return redirect("/")
