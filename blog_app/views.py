from django.shortcuts import render
from blog_app.models import Post

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
