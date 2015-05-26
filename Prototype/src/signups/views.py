from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect

from os import listdir
from os.path import isfile, join

from .forms import SignUpForm

def home(request):
    return render_to_response("homepage.html",
                              locals(),
                              context_instance=RequestContext(request))

def get_started(request):
    return render_to_response("get_started.html",
                              locals(),
                              context_instance=RequestContext(request))

def revenue_model(request):
    return render_to_response("revenue_model.html",
                              locals(),
                              context_instance=RequestContext(request))    

def contact(request):
    return render_to_response("contact.html",
                              locals(),
                              context_instance=RequestContext(request))

def en(request):
    return render_to_response("en_homepage.html",
                              locals(),
                              context_instance=RequestContext(request))

def signup_page(request):     
    
    form = SignUpForm(request.POST or None)
    
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
    
    return render_to_response("signup_page.html",
                              locals(),
                              context_instance=RequestContext(request))