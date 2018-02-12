from django.shortcuts import render
from django.views import generic
# Create your views here.

#models

from .models import School



class IndexView(generic.ListView):
    model = School
    template_name = "management_app/index.html"
