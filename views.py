from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from blog.models import Post
from django.core.paginator import Paginator
from .forms import CommentForm, PostForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.db.models import Q



# Create your views here.
    
@login_required
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username = username).exists():
            messages.error(request, 'invalid username')
            return redirect('login')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('post_list')
        messages.error(request,'OOps!')
    return render(request, 'blog/login.html')

def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username=username)
        
        if user:
            messages.info(request, 'Username already exist')
            return redirect('register')
        user = User.objects.create_user(
            username=username
        )
        user.set_password(password)
        user.save()
        # send.mail()
        messages.info(request, 'Account created successfully')
        return redirect('login')
    return render(request, 'blog/register.html')

def logout_page(request):
    logout(request)
    return redirect('post_list')
        
    

def post_list(request):
    search_query = request.GET.get('q')
    posts = Post.objects.all()
    if search_query:
        posts = posts.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'blog/post_list.html', context)



def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.filter()
    new_comment = None
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm(data=request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.post = post
                new_comment.author = request.user
                new_comment.save()
        else:
            form = CommentForm()
    else:
        form = None
    
    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'form': form
    }
    return render(request, 'blog/post_detail.html', context)

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_create.html', {'form': form})
   

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    context = {
        'posts': post,
    }
    return render(request, 'blog/post_list.html',  context)
