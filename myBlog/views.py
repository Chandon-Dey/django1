from django.shortcuts import render
from .models import Posts

# Create your views here.

def postPage(request):
    allposts = Posts.objects.all()

    postContent = {
        'posts': allposts,
    }
    return render(request, 'index.html', postContent)