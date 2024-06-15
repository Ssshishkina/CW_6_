from django import forms
from blog.models import Blog
from newsletter.forms import StyleFormMixin


class BlogForm(StyleFormMixin, forms.ModelForm):
    '''Класс стилизации формы Блога.'''
    class Meta:
        model = Blog
        exclude = ('preview',)
