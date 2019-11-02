from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Board
from .forms import BoardForm
from django.shortcuts import redirect
from datetime import datetime

def home(request):
    return render(request, 'board/index.html', {})

def board_list(request):
    posts = Board.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'board/post_list.html', {'posts': posts})

def post_detail(request, pk):
    posts = Board.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    post = get_object_or_404(Board, pk=pk)
    return render(request, 'board/post_detail.html', {'post':post, 'posts':posts})

def post_new(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            current = datetime.today()
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = current.strftime('%Y-%m-%d')
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = BoardForm()
    return render(request, 'board/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Board, pk=pk)
    if request.method == "POST":
        form = BoardForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = BoardForm(instance=post)
    return render(request, 'board/post_edit.html', {'form': form})

# Create your views here.
