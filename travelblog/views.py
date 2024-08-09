from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Post
from .forms import PostForm,PostUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "travelblog/index.html"

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "travelblog/post_detail.html",
        {"post": post},
    )

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()  # Save directly as form already includes author
            return redirect('home')  # Redirect to a list or detail view after saving
    else:
        form = PostForm()

    return render(
        request,
        'travelblog/post_form.html',
        {'form': form},
    )

def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'travelblog/post_edit.html', {'form': form, 'post': post})