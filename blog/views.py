from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.template import Context
from django.template import RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_protect
from contact import forms
from . import models as m
import datetime

def meta(request):
    return render_to_response('meta.html', {'items': request.META.items()})

def hello(request):
    return HttpResponse('%s: Welcome access %s'%(request.get_host(), request.META))

def systime(request):
    now = datetime.datetime.now()
    return render_to_response('hello.html', locals())

def current_time(request):
    now = datetime.datetime.now()
    t = get_template('current_time.html')
    html = t.render(Context({'current_time': now}))
    return HttpResponse(html)

def search(request):
    q = request.GET.get('q')
    errors = []
    if 'q' in request.GET:
        if not q:
            errors.append('Enter a not empty item.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = m.Book.objects.filter(title__icontains=q)
            return render_to_response('search_result.html', {'books': books, 'query': q})

    return render_to_response('search_form.html', {'error': errors})

@csrf_protect
def contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_date
            send_mail(
                cd['subject'],
                cd['content'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return render(request, 'hello.html')
    else:
        form = forms.ContactForm(initial={'subject': 'i love you'})
    return render_to_response('contact_form.html', {'form': form})

