from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def index(request):
	template=loader.get_template('core/index.html')
	context=dict()
	return HttpResponse(template.render(context, request))

def aboutme(request):
	template=loader.get_template('core/index.html')
	context=dict()
	return HttpResponse(template.render(context, request))

def quickfind(request):
	template=loader.get_template('core/index.html')
	context=dict()
	return HttpResponse(template.render(context, request))

def results(request):
	template=loader.get_template('core/index.html')
	context=dict()
	return HttpResponse(template.render(context, request))

def organization(request, org_name):
	template=loader.get_template('core/index.html')
	org=Organization.objects.get(name=org_name)
	context={'organization' : org}
	return HttpResponse(template.render(context, request))

def photo(request,photoname):
    image_data = open("photos/None/"+photoname, "rb").read()
    return HttpResponse(image_data, content_type="image/png")