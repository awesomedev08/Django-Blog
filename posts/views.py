from re import template
from django.views.generic import DetailView, ListView
from .models import Post, Category

class BlogDetail(DetailView):
    model = Post 
    context_object_name = 'post'
    template_name = 'posts/show-blog.html'

class BlogList(ListView):
    template_name = 'posts/index.html'
    context_object_name = 'posts'
    model = Post 

class PostCategories(ListView):
    """
    Show Posts by Category
    """
    template_name = 'posts/index.html'
    context_object_name = 'posts'
    model = Post 
    
    def get_queryset(self):
        return self.model.objects.filter(categories__name=self.kwargs.get('slug').title()).all()

class ListCategories(ListView):
    template_name = 'posts/list-categories.html'
    model = Category
    context_object_name = 'categories'

    def get_queryset(self):
        return self.model.objects.all().order_by('-name').reverse()
