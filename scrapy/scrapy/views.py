from django.shortcuts import render
from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.http import *
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from datetime import datetime,timedelta
import random,string

def home(request):
	if request.POST:
		name = request.POST['name']
		message = request.POST['message']
		email = request.POST['email']
		send_mail(name + "    " + email, message,"letsgetscrapy@gmail.com","<aakashchandhoke.24@gmail.com>", fail_silently=False)
	return render_to_response('index.html')

def greeting(request):
	return render_to_response('greeting.html')

def collages(request):
	return render_to_response('collages.html')

def scrapbook(request):
	return render_to_response('scrapbook.html')

def photograph(request):
	return render_to_response('photograph.html')