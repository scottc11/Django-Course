from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post

# '@login_required' ensures the user can only access below function/page if user is logged in
@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url']:
            post = Post()
            post.title = request.POST['title']

            # error check the url string
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                post.url = request.POST['url']
            else:
                post.url = 'http://' + request.POST['url']

            post.pub_date = timezone.datetime.now()
            post.author = request.user
            post.save()
            return redirect('home')
        else:
            return render(request, 'posts/create.html', {'error': 'ERROR: please provide both a title and a url to create a post.'})
    else:
        return render(request, 'posts/create.html')


def home(request):
    # go get all the posts and order them by 'votes_total'
    posts = Post.objects.order_by('votes_total')
    return render(request, 'posts/home.html', {'posts':posts})

def upvote(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.votes_total += 1
        post.save()
        return redirect('home')

def downvote(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.votes_total -= 1
        post.save()
        return redirect('home')
