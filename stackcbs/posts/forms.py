from django import forms
from .models import Post, Comment

class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs = {'rows':3}))
    class Meta:     #indicate the model
        model = Post
        fields = ('content',)
        #fields = ('content','image')

class CommentModelForm(forms.ModelForm):
    body = forms.CharField(label = "", widget=forms.TextInput(attrs = {'placeholder':"Add you replies here.."}))
    class Meta:
        model = Comment
        fields = ('body',)

  