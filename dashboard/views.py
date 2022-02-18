from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.decorators import method_decorator

from django.views.generic import (
                                FormView, 
                                UpdateView, 
                                ListView, 
                                DeleteView)
from django.db.models import Q
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView

from .forms import BlogForm, ProfileForm, ChangePasswordCustom, ImageUploads
from posts.models import Post, Images
import os 

@login_required(login_url='/account/login')
def index_dashboard(request):
    return render(request, template_name='dashboard/index.html')

@login_required(login_url='/account/login')
def logout_user(request):
    logout(request)
    messages.warning(request, 'Logged out')
    return redirect(reverse('account:login_page'))

class AddBlog(FormView):

    template_name = 'dashboard/add-blog.html'
    form_class = BlogForm

    def get_success_url(self, **kwargs) -> str:
        return reverse('dashboard:edit_blog', kwargs={'pk':kwargs.get('pk')})
    
    def form_valid(self, form):
        result = form.save(commit=False)
        result.author = self.request.user 
        result.save()
        
        messages.success(self.request, 'Blog Added')
        return redirect(self.get_success_url(pk=result.pk))
    
    @method_decorator(login_required(login_url='/account/login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class UpdateBLog(UpdateView):
    model = Post 
    form_class = BlogForm
    template_name = 'dashboard/add-blog.html'

    def get_success_url(self) -> str:
        return reverse('dashboard:edit_blog', args=(self.kwargs.get('pk'),))
    
    @method_decorator(login_required(login_url='/account/login'))
    def dispatch(self, request, *args, **kwargs):
        try:
            result = self.get_object()
            if result.author != request.user and (not request.user.is_superuser and result.edit_permission != 0):
                return redirect(reverse('dashboard:add_blog'))
        except Exception as e:
            print(e)
            return redirect(reverse('dashboard:add_blog'))
        return super().dispatch(request, *args, **kwargs)

class ListsBlog(ListView):
    model = Post 
    template_name = 'dashboard/lists-blog.html'
    context_object_name = 'blog_lists'
    paginate_by = 7

    @method_decorator(login_required(login_url='/account/login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            result = self.model.objects.all()
        else:
            result = self.model.objects.filter(
                    Q(author=self.request.user) | Q(edit_permission=0)
            )
        return result

class DeleteBlog(DeleteView):
    model = Post 
    template_name = 'dashboard/delete-blog.html'

    def get_success_url(self) -> str:
        return reverse('dashboard:lists_blog')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.model.objects.get(pk=self.kwargs.get('pk')).title
        return context
    
    def form_valid(self, form):
        self.object = self.get_object()
        if os.path.exists(self.object.img.path):
            os.remove(self.object.img.path)
        self.object.delete()
        return redirect(self.get_success_url())

class Profile(UpdateView):
    template_name = 'dashboard/profile.html'
    model = User 
    form_class = ProfileForm

    def get_success_url(self) -> str:
        return reverse('dashboard:profile', kwargs={'pk':self.request.user.pk})
    
    def dispatch(self, request, *args, **kwargs):
        """
        validating, if user visit another edit profile page user, 
        it will be redirecting to user edit profile page 
        """
        if request.user.pk != self.kwargs.get('pk') and not request.user.is_superuser:
            return redirect(reverse('dashboard:profile', kwargs={'pk':request.user.pk}))
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Profile Edited!')
        return super().form_valid(form)

class ChangePassword(PasswordChangeView):
    form_class = ChangePasswordCustom
    template_name = 'dashboard/change-password.html'

    def get_success_url(self) -> str:
        return reverse('dashboard:change_password')
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            update_session_auth_hash(request, request.user)
        return super().post(request, *args, **kwargs)

class UploadImage(FormView):
    model = Images
    form_class = ImageUploads
    template_name = 'dashboard/upload-images.html'
    
    def get_success_url(self) -> str:
        return reverse('dashboard:list_images')
    
    def form_valid(self, form):
        ins = form.save(commit=False)
        ins.author = self.request.user 
        ins.save()
        
        return super().form_valid(form)

class ListImages(ListView):
    model = Images
    context_object_name = 'images'
    
    template_name = 'dashboard/list-images.html'

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)
    
