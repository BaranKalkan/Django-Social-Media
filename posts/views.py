from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.db.models import Count
from django.db.models import Exists, OuterRef

from .models import Comment, Post, PostLikes

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# ...

@login_required
def results(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/results.html', {'post': post})

class IndexView(LoginRequiredMixin,generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last five published questions."""
            
        return Post.objects.filter(
                pub_date__lte = timezone.now()
            ).annotate(num_likes=Count('likes')).annotate(is_liked=Exists(PostLikes.objects.filter(user=self.request.user,post_id=OuterRef('pk')))).order_by('-pub_date')[:5]

class DetailView(LoginRequiredMixin,generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Post.objects.filter(pub_date__lte=timezone.now())

class UserPostsView(LoginRequiredMixin,generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'latest_post_list'
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Post.objects.filter(pub_date__lte=timezone.now()).filter(owner = self.request.user).order_by('-pub_date')


class ResultsView(LoginRequiredMixin,generic.DetailView):
    model = Post
    template_name = 'posts/results.html'
   

"""
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
"""

@login_required
def vote(request, post_id):
    return HttpResponse("You're commenting on post %s." % post_id)