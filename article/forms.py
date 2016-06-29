from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(label="标题", max_length=100)
    content = forms.CharField(label="内容", max_length=10000)
