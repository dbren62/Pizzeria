from django import forms
from .models import Pizza, Topping

class CommentForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['name']
        label = {'Comment: ':''}