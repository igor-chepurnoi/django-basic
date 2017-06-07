from project.apps.auth.forms.signup_form import SignUpForm
from django.contrib.auth import login
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.authenticate()
            login(request, user)

            return redirect('index')

    else:
        form = SignUpForm()

    return render(request, 'auth/signup.html', {
        'form': form,
    })
