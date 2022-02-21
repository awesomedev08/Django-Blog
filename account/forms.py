from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column

class RegisterForm(UserCreationForm):

    class Meta:
        model = User 
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].help_text = False 

        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            'first_name',
            'last_name',
            'password1',
            'password2'
        )
        self.helper.help_text_inline = False
        self.helper.error_text_inline = False 
        self.helper.add_input(Submit('submit', 'Register'))
    
    username = forms.CharField(min_length=5, required=True)
    

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('login','Login'))
