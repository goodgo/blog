# -*- coding:utf-8 -*-

from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False, label='your e-mail address')
    content = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        if 4 > len(message.split()):
            raise forms.ValidationError('Not enought Words')
        return message

if __name__ == '__main__':
    c = ContactForm()
    print c
