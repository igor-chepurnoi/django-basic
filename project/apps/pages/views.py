from project.apps.pages.forms.contact_form import ContactForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _


def index(request):
    return render(request, 'pages/index.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            if form.contact():
                messages.success(request, _('Thank you for contacting us. We will respond to you as soon as possible.'))
            else:
                messages.error(request, _('There was an error sending email.'))

            return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {
        'form': form,
    })
