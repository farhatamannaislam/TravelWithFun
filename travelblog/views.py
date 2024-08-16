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
    Display an individual :model:`travelblog.Post`.

    **Context**

    ``post``
        An instance of :model:`travelblog.Post`.

    **Template:**

    :template:`travelblog/post_detail.html`
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
    """
    Create a Post.

    **Context**

    ``form``
        An instance of :form:`travelblog.PostForm`.

    **Template:**

    :template:`travelblog/post_form.html`
    """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(
        request,
        'travelblog/post_form.html',
        {'form': form},
    )
@login_required
def post_edit(request, slug):
    """
    Edit a Post.

    **Context**

    ``form``
        An instance of :form:`travelblog.PostForm`.
    ``post``
        An instanece of :model:'travelblog.Post'

    **Template:**

    :template:`travelblog/post_edit.html`
    """ 
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'travelblog/post_edit.html', {'form': form, 'post': post})

@login_required
def post_delete(request, slug):
    """
    Delete a Post.

    **Context**
    ``post``
        An instanece of :model:'travelblog.Post'

    **Template:**

    :template:`travelblog/post_delete.html`
    """ 
    post = get_object_or_404(Post, slug=slug)
    
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    
    return render(request, 'travelblog/post_delete.html', {'post': post})