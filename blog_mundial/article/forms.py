from django import forms

class ArticleForm(forms.Form):
    name = forms.CharField(max_length=40, label='Nombre')
    country = forms.CharField(max_length=20, label='País')
    article_id = forms.IntegerField(label='Numero de artículo')
    article_content = forms.TextInput()