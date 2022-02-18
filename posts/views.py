from django.views.generic import DetailView, ListView
from .models import Post

class BlogDetail(DetailView):
    model = Post 
    context_object_name = 'post'
    template_name = 'posts/show-blog.html'

class BlogList(ListView):
    template_name = 'posts/index.html'
    context_object_name = 'posts'
    model = Post 
