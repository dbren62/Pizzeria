from django import forms
from .models import Pizza, Topping, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        label = {'text: ':''}

        widgets = {'text': forms.Textarea(attrs={'cols':50})}
"""
from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    #Form for the image model
    class Meta:
        model = Image
        fields = ('title', 'image')
"""