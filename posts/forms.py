#-*- coding: utf-8 -*-
from django import forms
from pagedown.widgets import PagedownWidget
from .models import Post


class PostForm(forms.ModelForm):
    # 1) добавим поля после установки pagedown для редактирования текста в форме
    # https://github.com/timmyomahony/django-pagedown 'content, publish'
    # 2) в base.html вставим блок {%lock head_extra%}
    content = forms.CharField(widget=PagedownWidget(show_preview=False))# виджет добавится к полю контент
    publish = forms.DateField(widget=forms.SelectDateWidget)# виджет добавится к полю дата публикации
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image",
            "draft",
            "publish",
        ]