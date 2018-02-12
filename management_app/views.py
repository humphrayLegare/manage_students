#from django.shortcuts import render
from django.views import generic
#from django.urls import reverse

# Create your views here.

#models

from .models import School



class IndexView(generic.ListView):
    model = School
    template_name = "management_app/index.html"
    context_object_name = 'latest_school_list'

    def get_queryset(self):
        return School.objects.all()

class DetailView(generic.DetailView):
    model = School
    template_name = 'management_app/detail.html'
