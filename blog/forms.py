from django import forms
from blog.models import Comment,Post

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('author', 'text','approved_comment',)

