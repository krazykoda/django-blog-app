from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
def blog_index(request):
	posts = Post.objects.all().order_by('created_on')

	data = {
		"posts": posts,
	}

	return render(request, 'index.html', data)


def blog_detail(request, pk):
	user =  request.user
	post = Post.objects.get(pk=pk)
	comments = Comment.objects.filter(post=post)

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = Comment(
				body = form.cleaned_data["body"],
				author = user,
				post = post
			)

			comment.save()			
	else:
		form = CommentForm()

	data = {
		"post": post,
		"form": form,
		"comments": comments
	}

	return render(request, 'detail.html', data)

@login_required(login_url='login')
def create(request):
	user =  request.user
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = Post(
				title = form.cleaned_data["title"],
				body = form.cleaned_data["body"],
				author = user
			)

			post.save()			
			return redirect("/blogs")
	else:
		form = PostForm()

	data = {
		"form": form
	}
	return render(request, 'create.html', data )


def edit(request, pk):
	pass


