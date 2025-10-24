from django.shortcuts import render

from django.views.generic import DetailView, CreateView
from django.views.generic.base import TemplateView

from studens.models import Student
from custom_admin.forms import StudentModelForm


class MainAdminView(TemplateView):
    template_name = 'custom_admin/main.html'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'custom_admin/student_detail.html'
    context_object_name = 'student'  


class StudentCreateView(CreateView):
    model = Student
    template_name = 'custom_admin/student_create.html'
    form_class = StudentModelForm