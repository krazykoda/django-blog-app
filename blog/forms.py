from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment


class PostForm(forms.Form):
	title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
			"class": "form-control",
			"placeholder": "Enter Title"
		}))
	body = forms.CharField(widget=forms.Textarea(attrs={
			"class": "form-control",
			"placeholder": "Post goes here..."
		}))


class CommentForm(forms.Form):
	body = forms.CharField(label = "", widget=forms.Textarea(attrs={
			"class": "form-control",
			"placeholder": "Leave a Comment"
		}))


