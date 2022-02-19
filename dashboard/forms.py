from random import choices
from django.forms import ModelForm
from django import forms 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from posts.models import Post, Category, Images

from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class BlogForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit','Add Blog '))
    
    class Meta:
        model = Post 
        fields = ('title','edit_permission','categories','body_text', 'img')
    
    edit_permission = forms.ChoiceField(required=False, 
                                        choices=(
                                            (0,'Anyone can edit'),
                                            (1,'Only admin and you can edit')
                                        )
                    )
    
    categories = forms.ModelMultipleChoiceField(required=False, 
                                        queryset=Category.objects.all(),
                                        widget=forms.CheckboxSelectMultiple)
    
    body_text = forms.Textarea(attrs={'id':'editor1'})
    title = forms.CharField(min_length=20, max_length=60)
    img = forms.ImageField(required=False)

class ProfileForm(ModelForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        for field in self.fields:
            self.fields[field].help_text = False 
        
        self.helper.add_input(Submit('submit', 'Submit'))

    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
    
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    username = forms.CharField(required=False)

class ChangePasswordCustom(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit','Change'))
        
        for field in self.fields:
            self.fields[field].help_text = False 

class ImageUploads(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit','Add Images'))

    class Meta:
        model = Images    
        fields = ('name', 'img')
    

