from smtplib import SMTPResponseException

from captcha.fields import CaptchaField
from django import forms
from django.conf import settings
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    body = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    captcha = CaptchaField(label='Verification Code')

    def contact(self):
        subject = self.cleaned_data['subject']
        from_email = self.cleaned_data['email']
        message = self.cleaned_data['body']

        try:
            return send_mail(subject, message, from_email, settings.ADMINS)
        except SMTPResponseException:
            return False
