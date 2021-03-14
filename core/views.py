from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.template import loader
import random

from .models import Tag, Tag_Type, Arching_Tag, Organization, Response, Quote



def index(request):
	template=loader.get_template('core/index.html')
	context=dict()
	return HttpResponse(template.render(context, request))


def addtag(request, instance, metatag, addedtag):
	r = Response.objects.get(pk=instance)
	tag = Tag.objects.get(name=addedtag)
	meta = Tag_Type.objects.get(name=metatag)
	r.tags_selected.add(tag)
	r.tags_completed.add(meta)
	return redirect('/aboutme/'+str(instance))


def aboutme(request, instance=None):
	if instance==None:
		r = Response()
		r.save()
		return redirect('aboutme/'+str(r.id))

	else:
		r = Response.objects.get(pk=instance)

		tags_list = Tag_Type.objects.all()
		tags_list = [tag.name for tag in tags_list]

		completed_tags = r.tags_completed.all()
		completed_tags = [tag.name for tag in completed_tags]



		for tag in tags_list:
			if tag not in completed_tags:
				tag_obj = Tag_Type.objects.get(name=tag)

				question = tag_obj.question
				choices = Tag.objects.filter(tag_type__name=tag)
				color = tag_obj.color
				all_quotes = Quote.objects.all()
				quote = random.choice([obj.words for obj in all_quotes])

				template=loader.get_template('core/aboutme.html')
				context={
					'question':question,
					'choices':choices,
					'quote':quote,
					'color':color,
					'pkid' : r.id,
					'metatag' : tag
					}
				return HttpResponse(template.render(context, request))

		else:
			template=loader.get_template('core/results.html')
			context={
				}
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
		'organizations': Organization.objects.filter(overall_tags__name=arching_name),
		'tag':arching_name
	}
	return HttpResponse(template.render(context, request))

def results_tagspecific(request, tag_name,semi_name):
	template=loader.get_template('core/results.html')
	context={
		'organizations': Organization.objects.filter(tags__name=tag_name),
		'tag':tag_name,
		'seminame':semi_name
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