from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm

# Create your views here.
def register(request):
	if request.user.is_authenticated:
		return redirect('blog')
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('blog')
	else:
		form = RegistrationForm()

	return render(request, 'registration/register.html', {"form": form})






