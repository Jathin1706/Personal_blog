from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm 

from django.urls import reverse_lazy
from django.contrib.auth import logout


class Register(generic.CreateView):
    form_class=UserCreationForm
    template_name='registration/register.html'
    success_url=reverse_lazy('login')


