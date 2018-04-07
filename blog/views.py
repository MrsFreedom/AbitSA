from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Teacher
from django.shortcuts import render, get_object_or_404
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def teacher(request):
    teachers = Teacher.objects.all()
    return render(request, 'blog/teacher.html', {'teachers': teachers})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
def bacalavr(request):
    return render(request, 'blog/bacalavr.html')
def magistr(request):
    return render(request, 'blog/magistr.html')
def aspir(request):
    return render(request, 'blog/aspir.html')
def prog_bac(request):
    return render(request, 'blog/prog_bac.html')
def mentor_detal(request,pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'blog/mentor_detal.html', {'teachers': teacher})
def home(request):
    return render(request, 'blog/home.html')
def map(request):
    return render(request, 'blog/map.html')