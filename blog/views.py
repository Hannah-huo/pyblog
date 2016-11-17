from django.shortcuts import render
from blog.models import User

def index(req):
    context = {}
    context['title'] = 'Index'
    context['message'] = 'Content from server'
    return render(req, 'index.html', context)

def signin(req):
    #should add cookie support here
    context = {}
    context['title'] = 'Sign In'
    return render(req, 'signin.html', context)

def signup(req):
    context = {}
    context['title'] = 'Sign Up'
    return render(req, 'signup.html', context)

def list_blogs(req):
    context = {}
    return render(req, 'list.html', context)

def process_signin(req):
    context = {}
    context.update(csrf(req))
    