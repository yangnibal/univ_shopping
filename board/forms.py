from django import forms
from .models import Board
from django.contrib.auth.models import User

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs = {
                'class': 'form-title', 
                'placeholder':'제목을 입력해주세요.'
            }),
            'content': forms.TextInput(attrs = {
                'class': 'form-content',
                'placeholder':'내용을 입력해주세요.'
            })
        }
        labels = {
            'title':'제목',
            'content':'내용'
        }

