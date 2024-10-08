from django.shortcuts import render, get_object_or_404
from blog_app.models import Post
from django.contrib.auth.models import User
# import ListView from generic:
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)

# if we're going to use HttpResponse, we will do like this :
# from django.http import HttpResponse
# def home(request):
#     return HttpResponse("<h1> Blog HomePage </h1>")
# def about(request):
#     return HttpResponse("<h1> Blog About Page </h1>")

# dummy_posts = [
#     {
#         "author": "Ahmed",
#         "title": "My Third Primary Grade",
#         "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
#         "date_posted": "July 10, 2023"
#     },    
#     {
#         "author": "Ibrahim",
#         "title": "My Sixth Primary Grade",
#         "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
#         "date_posted": "July 11, 2023"
#     },
# ]



def home(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html", {"title": "About Page"})


## the pattern that url looks for to display the page correctly is :
# <app>/<model>_<viewtype>.html ==> blog_app/Post_List.html


## list all posts
class PostListView(ListView):
    ''' We have taken a new class that inherits directly from ListView, and inside
    it we have to define the model which we want to do (crud ops) on it '''
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 4

## go to user posts page
class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = "posts"
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-date_posted")


## one single post detail
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post-detail.html"
    context_object_name = "posts"

## create new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/post_form.html"
    context_object_name = "posts"
    title = "Create Post"


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # if you want to pass "title" to create template in class-based views
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Post"
        return context


## update existing post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/post_form.html"
    context_object_name = "posts"
    title = "Update Post"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # if the login user is the same as the author of the post, then delete it
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    # if you want to pass "title" to update template:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Post"
        return context

## delete existing post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    context_object_name = "posts"
    # after deleting the post, go to home-page
    success_url = "/"
    # if the login user is the same as the author of the post, then delete it
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False