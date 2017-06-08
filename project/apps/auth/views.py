from django.contrib.auth import login
from django.shortcuts import render, redirect

from project.apps.auth.forms.signup_form import SignUpForm


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.authenticate()
            login(request, user)

            return redirect('home')

    else:
        form = SignUpForm()

    return render(request, 'auth/signup.html', {
        'form': form,
    })
