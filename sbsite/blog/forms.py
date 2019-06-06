from django import forms
from django.forms import ModelForm
from .models import Post

# from django import forms
# from .models import Post, Images

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['content','content2']
# class PostForm(forms.ModelForm):
#     title = forms.CharField(max_length=128)
#     content = forms.CharField(max_length=245, label="content")
    
#     class Meta:
#         model = Post
#         fields = (
#             'title',
#             'content',
#              )

        
# class ImageForm(forms.ModelForm):
#     image = forms.ImageField(label='image')
#     class Meta:
#         model = Images
#         fields = ('image',)
        

class UserLoginForm(forms.Form):
    username = forms.CharField(label="")
    password = forms.CharField(label="", widget=forms.PasswordInput)
    