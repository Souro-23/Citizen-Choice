from django.shortcuts import render, redirect,  HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import PostsArticle, FeedPosts
from django.utils import timezone
from .forms import Post_Article
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.views.generic import UpdateView, CreateView
from django import forms
from django.contrib.auth.models import User
from .forms import Post_Article
from django.views.generic.edit import FormView
from hashing.views import create_hash
# Create your views here.





class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin , UpdateView):
    login_url = '/login/'
    model = PostsArticle
    fields= ['title', 'abstract', 'body', 'image']
    template_name= 'post/edit_post.html'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Posts = self.get_object()
        if self.request.user == Posts.user:
            return True
        return False


class FeedUpdateView(LoginRequiredMixin, UserPassesTestMixin , UpdateView):
    login_url = '/login/'
    model = FeedPosts
    fields= ['body', 'image']
    template_name= 'post/edit_Feed.html'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Posts = self.get_object()
        if self.request.user == Posts.user:
            return True
        return False

class PostCreateView(LoginRequiredMixin,FormView):
    login_url = '/login/'
    form_class = Post_Article
    template_name= 'post/post.html'
    success_url =  '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.hash_tags = form.instance.hash_tags.lower()
        form = form.save()
        create_hash(form.hash_tags,form.id,"postsarticle")
        return super().form_valid(form)



def PostCreateFeedView(request):
    form = create_feed_form(request.POST)
    model = FeedPosts()

    if form.is_valid():
        model.user = request.user
        model.body = form.cleaned_data['body']
        model.image = request.FILES['image']
        model.save()

    return redirect('home')


class create_feed_form(forms.ModelForm):
    class Meta:
        model = FeedPosts
        fields= [ 'body', 'image' ]

def get_feeds(request):
    feeds = FeedPosts.objects.all()
    return feeds
