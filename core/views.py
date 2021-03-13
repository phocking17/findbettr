from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Tag, Tag_Type, Arching_Tag, Organization



def index(request):
	template=loader.get_template('core/index.html')
	context=dict()
	return HttpResponse(template.render(context, request))

def aboutme(request):
	template=loader.get_template('core/index.html')
	context=dict()
	return HttpResponse(template.render(context, request))

def quickfind(request):
	template=loader.get_template('core/quickfind.html')
	context={
		'tags' : [[tags, Tag.objects.filter(tag_type=tags)] for tags in Tag_Type.objects.all()],
		'arching_tag': Arching_Tag.objects.all(),
		}
	return HttpResponse(template.render(context, request))

def results_general(request, arching_name):
	template=loader.get_template('core/results.html')
	context={
		'organizations': Organization.objects.filter(overall_tags__name=arching_name)
	}
	return HttpResponse(template.render(context, request))

def results(request):
	template=loader.get_template('core/results.html')
	context={
		'organizations':Organization.objects.filter(overall_tags=arching_name)
	}
	return HttpResponse(template.render(context, request))

def organization(request, org_name):
	template=loader.get_template('core/index.html')
	org=Organization.objects.get(name=org_name)
	context={'organization' : org}
	return HttpResponse(template.render(context, request))

def photo(request,photoname):
    image_data = open("photos/None/"+photoname, "rb").read()
    return HttpResponse(image_data, content_type="image/png")