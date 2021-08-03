from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout,authenticate
from blogApp.models import Post
from django.db.models import Max

# Create your views here.
def home(request):
    
    post = Post.objects.all()
    post = Post.objects.order_by('-views')
    context = {"posts":post[0:6]}
    return render(request, 'home/index.html',context)

def about(request):
    return render(request, 'home/about.html')
    
def contactus(request):
    if request.method=='POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        newcontact = Contact(name=name, phone=phone, email=email, desc=desc)
        newcontact.save()
        messages.success(request, 'Your message has been delivered! \n we will look for it shortly.')

    return render(request, 'home/contactus.html')

def blogs(request):
    return render(request, 'blogHome/blogHome.html')

def login_user(request):
    if request.method=='POST':
        username = request.POST.get('loginusername')
        password = request.POST.get('loginpassword')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")

def logout_user(request):
    logout(request)
    return redirect("home")

def signup(request):
    if request.method == 'POST':
        fname =  request.POST['fname']
        lname =  request.POST['lname']
        email =  request.POST['email']
        username =  request.POST['username']
        password =  request.POST['pass1']
        cpass =  request.POST['pass2']
        if password == cpass:
            user = User.objects.create_user(username, email, password)
            user.first_name = fname
            user.last_name = lname
            user.save()
            messages.success(request, "welcome you're a user now")
        else:
            messages.warning(request,"password did't matched ")
    return redirect("home")

def search(request):
    query = request.GET['query']
    if len(query) >=50:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostscontent = Post.objects.filter(content__icontains=query)
        allPostsAuthor = Post.objects.filter(author__icontains=query)
        allPosts = allPostsTitle.union(allPostscontent,allPostsAuthor)

    params={"allPosts":allPosts, "query": query}
    return render(request,'home/search.html',params)

def user_profile(request):
    return render(request, 'home/user_profile.html')

def edit_profile(request):
    return render(request, 'home/edit_profile.html')

def user_blogs(request):
    user = request.user
    allPosts = Post.objects.filter(author__icontains=user)
    context = {"posts":allPosts, "user":user}
    return render(request, 'home/user_blogs.html',context)
