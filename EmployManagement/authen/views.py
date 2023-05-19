from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, auth
from myapp.models import *
# Create your views here.

def signIn(request):
    if request.method == 'POST':
        u_name = request.POST['usrname']
        passwrd = request.POST['pass']
        user = auth.authenticate(username=u_name, password=passwrd)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
    return render(request,'login.html')


def log_out(request):
    logout(request)
    return redirect('login')


###### user management ######

def user_index(request):
    users = CustomUser.objects.all()
    services = Service.objects.all()
    posts = Post.objects.all()
    return render(request, 'user.html',{'users':users,'services':services,'posts':posts})


# list all users
def all_users(request):
    users = CustomUser.objects.all()
    return render(request,'userList.html',{'users':users})

# user details
def user(request, pk):
    user = CustomUser.objects.get(id = pk)
    return render(request, 'user_detail.html',{'user':user})

#add a user
def add_user(request):
    services = Service.objects.all()
    posts = Post.objects.all()
    if request.method == 'POST':
        u_name = request.POST['name']
        f_name = request.POST['fname']
        l_name = request.POST['lname']
        mail = request.POST['mail']
        tel = request.POST['tel']
        birth_date = request.POST['birth_date']
        birth_place = request.POST['birth_place']
        sex = request.POST['sex']
        matrim = request.POST['matrimonial']
        u_service = request.POST['service']
        u_post = request.POST['post']
        for service in services:
            if service.name == u_service:
                serv = service
        for post in posts:
            if post.name == u_post:
                pos = post
        user = CustomUser(
            username = u_name,
            first_name = f_name,
            last_name = l_name,
            email = mail,
            date_of_birth = birth_date,
            birth_place = birth_place,
            sex = sex,
            matrimonial_situation = matrim,
            service = serv,
            post = pos
        )
        user.save()
        return redirect('/users/') 
    return render(request,'add_user.html', {'services':services,'posts':posts})

# add user to service
def add_user_service(request, pk):
    service = Service.objects.get(id=pk)
    posts = Post.objects.all()
    if request.method == 'POST':
        u_name = request.POST['name']
        f_name = request.POST['fname']
        l_name = request.POST['lname']
        mail = request.POST['mail']
        tel = request.POST['tel']
        birth_date = request.POST['birth_date']
        birth_place = request.POST['birth_place']
        sex = request.POST['sex']
        matrim = request.POST['matrimonial']
        u_post = request.POST['post']
        for post in posts:
            if post.name == u_post:
                pos = post
        user = CustomUser(
            username = u_name,
            first_name = f_name,
            last_name = l_name,
            email = mail,
            date_of_birth = birth_date,
            birth_place = birth_place,
            sex = sex,
            matrimonial_situation = matrim,
            service = service,
            post = pos
        )
        user.save()
        return redirect('/service/'+str(service.id))
    return render(request,'add_user_service.html',{'service':service,'posts':posts})

# update a user info
def update_user(request, pk):
    user = CustomUser.objects.get(id = pk)
    return

#delete a user
def delete_user(request, pk):
    user = CustomUser.objects.get(id = pk)
    user.delete()
    return redirect('/users/')
