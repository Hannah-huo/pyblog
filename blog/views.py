from django.shortcuts import render

def index(req):
    context = {}
    context['title'] = 'Index'
    context['message'] = 'Content from server'
    return render(req, 'index.html', context)

def list_blogs(req):
    context = {}
    return render(req, 'list.html', context)