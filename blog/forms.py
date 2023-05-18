from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control my-2'
            field.field.widget.attrs['placeholder'] = field.field.label

    class Meta:
        model = Post
        exclude = ['author', 'created_at', 'updated_at']