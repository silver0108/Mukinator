from django import forms
from community.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['subject', 'content', 'region']
        labels = {
            'subject': '제목',
            'content': '내용',
            'region': '지역',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '내용',
        }
