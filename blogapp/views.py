from django.shortcuts import render, redirect
from .models import Post
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import( 
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView
    )
# Create your views here.

# Home page view
def home(request):
    context = {
        "posts":Post.objects.all()
    }
    return render(request, 'blogapp/home.html',context,status=201,)


# Class based view for posts list at home page
class PostListView(ListView):

    # Dealing with post model 
    model = Post
    template_name = 'blogapp/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4

# To get post details for a perticular post
class PostDetailsView(DetailView):
    # Dealing with post model 
    model = Post
    
# To create new post 
class PostCreateView(LoginRequiredMixin, CreateView):
    # Dealing with post model 
    model = Post

    # Fields in the post we have to save
    fields = ["title","content"]

    # Check for the validity
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Inorder to update the post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # Dealing with post model 
    model = Post
    fields = ["title","content"]
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Test user is authenticated or not before update 
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    success_url = "/"

    # Test user is authenticated or not before delete
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# TO get the all post for a user
class PostListUserView(ListView):
    model = Post
    template_name = 'blogapp/post_per_user.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2

# To about view
def about(request):
    return render(request, 'blogapp/about.html')