from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect

from os import listdir
from os.path import isfile, join

from .forms import SignUpForm

def home(request):
    return render_to_response("homepage_lang.html",
                              locals(),
                              context_instance=RequestContext(request))

def en(request):
    return render_to_response("en_homepage.html",
                              locals(),
                              context_instance=RequestContext(request))

def signup_page():     
    form = SignUpForm(request.POST or None)
    
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
    
    return render_to_response("signup.html",
                              locals(),
                              context_instance=RequestContext(request))