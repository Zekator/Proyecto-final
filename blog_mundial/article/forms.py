from django import forms

from ckeditor.fields import RichTextField


class ArticleForm(forms.Form):
    name = forms.CharField(max_length=40, label='Titulo')
    country = forms.CharField(max_length=20, label='País')
    article_id = forms.IntegerField(label='ID')
    article_content = forms.CharField(widget=forms.Textarea, label='Contenido')
    
