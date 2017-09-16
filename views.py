# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from datetime import datetime
from django.shortcuts import render

# Create your views here.

def index(request):
	currenttime = gmtime()

	context = {'day': strftime('%B %d, %Y', currenttime), 'time': strftime('%I:%M %p', currenttime)}
	return render(request, 'time_display/index.html', context)