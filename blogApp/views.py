from django.shortcuts import render, redirect
from blogApp.models import Post, BlogComment
from django.contrib import messages
# Create your views here.
def blogHome(request):
    allPosts = Post.objects.order_by('views')
    
    context = {"allPosts" : allPosts}
    return render(request, 'blogHome/blogHome.html',context)

def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    post.views= post.views +1
    post.save()
    comment = BlogComment.objects.filter(post=post)
    context = {"post":post, "comments":comment, "user":request.user}
    return render(request, 'blogHome/blogPost.html',context)

def addPost(request):
    if request.method == "POST":
        sno = request.POST.get('postSno')
        author = request.user
        title = request.POST.get('title')
        slug = title.replace(" ","-")
        content = request.POST.get('add_content') 
        post = Post(author=author,title=title,slug=slug,content=content)
        post.save()
        messages.success(request,"Posted")
    return render(request,'blogHome/addpost.html')

def postComment(request):
    if request.method == 'POST':
        postSno = request.POST.get('postSno')
        comments = request.POST.get('comments')
        user = request.user
        post = Post.objects.get(sno=postSno)
        comment = BlogComment(comment=comments, user=user,post=post)
        comment.save()
    return redirect(f"blogPost/{post.slug}")