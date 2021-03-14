from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("aboutme", views.aboutme, name='About Me'), 
    path("aboutme/<int:instance>", views.aboutme, name='About Me'),
    path("aboutme/<int:instance>/<str:metatag>/<str:addedtag>", views.addtag, name='AddTag'),
    path("quickfind", views.quickfind, name='QuickFind'), 
    path("results", views.results, name='Results'), 
    path("organization/<str:org_name>", views.organization, name='test org'),
    path("photos/None/<str:photoname>", views.photo, name="photos"),
    path("results/<str:arching_name>", views.results_general, name="results general"),
    path("results/<str:semi_name>/<str:tag_name>", views.results_tagspecific, name="results tagspecific")
]