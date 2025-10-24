from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.views.generic.base import TemplateView
from django_filters.views import FilterView

from studens.models import Student, Group
from custom_admin.forms import StudentForm, StudentModelForm
from studens.filters import StudentFilter


class AboutTemplateView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "About Page"
        return context


class MainTemplateView(TemplateView):
    template_name = "index.html"

   



class StudentListView(ListView):
    paginate_by = 1
    template_name = "index.html"
    model = Student
    


class StudentListFilter(FilterView):
    paginate_by = 1
    template_name = "index.html"
    model = Student
    filterset_class = StudentFilter

    



class StudentView(View):
    def get(self, request):
        students = Student.objects.all()
        search = request.GET.get('search')
        if search:
            students = Student.objects.filter(name__icontains=search)

        filter_set = StudentFilter(request.GET, queryset=students)

        page = request.GET.get('page', 1)
        limit = request.GET.get('limit', 2)

        paginator = Paginator(filter_set.qs, limit)
        students = paginator.get_page(page)

        return render(request, 'index.html', {"students": students})
    
    def post(self, request):
        name = request.POST.get('name')
        name = request.POST.get('name')
        name = request.POST.get('name')
        name = request.POST.get('name')
        Student.objects.create(name=name)
        return render(request, 'index.html')
    


def main(request):
    students = Student.objects.all()
    
    search = request.GET.get('search')
    
    if search:
        students = Student.objects.filter(name__icontains=search)

    filter_set = StudentFilter(request.GET, queryset=students)

    page = request.GET.get('page', 5)
    limit = request.GET.get('limit', 10)

    paginator = Paginator(filter_set.qs, limit)
    students = paginator.get_page(page)

    return render(request, 'index.html', {
        'students': students,         
        'is_paginated': students.has_other_pages(),
        'search': search,
        'filter': filter_set
    })


def student_detail(request, id):
    student = Student.objects.get(id=id)
    print(student)
    return render(request, 'student_detail.html', {'student': student})


def student_update(request, id: int):
    student = get_object_or_404(Student, id=id)
    groups = Group.objects.all()

    if request.method == "POST":
        print(request.POST)
        print(request.FILES)

        form = StudentModelForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
    
    form = StudentModelForm(instance=student)

    return render(request, 'student_update.html', {'student': student, 'groups': groups, "form": form})



def create_student(request):
    groups = Group.objects.all()
    form = StudentForm()
 
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            print("Post request")
            form_data = form.cleaned_data
            print(form_data)
            Student.objects.create(
                name=form_data.get("name"),
                last_name=form_data.get("last_name"),
                age=form_data.get("age"),           
                email=form_data.get("email"),
                phone_number=form_data.get("phone_number"),
                group=form_data.get("group"),
                avatar=form_data.get("avatar"),
                is_active=form_data.get("is_active"),
            )
           
            print("worked")
            return redirect("/")
        

    return render(request, 'student_create.html', {"groups": groups, "form": form})


def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("/")