from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import FileSystemStorage
from studens.models import Student, Group
from .forms import StudentModelForm, StudentForm
from .filters import StudentFilter
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView


class StudentView(View):
    def get(self, request):
        students = Student.objects.all()
        return render(request, 'index.html', {'students': students})
    
    
class StudentDetailView(View):
    def get(slef, request, id):
        student = get_object_or_404(Student, id=id)
        print(student)
        return render(request, 'index2.html', {'student': student})
    

class MainTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["students"] = Student.objects.all()
        context["title"] = 'Main Page'
        return context
    

class AboutTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["students"] = Student.objects.all()
        context["title"] = 'About Page'
        return context
    

class StudentCreateView(CreateView):
    model = Student
    template_name = 'create_student.html'
    form_class = StudentModelForm


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'update_student.html'
    form_class = StudentModelForm



class StudentDetailView(DetailView):
    model = Student
    template_name = 'index2.html'
    form_class = StudentModelForm





# class StudentCreateView(CreateView):
#     model = Student
#     template_name = 'create_student.html'
#     form_class = StudentModelForm

# def main(request):
#     students = Student.objects.all()
#     return render(request, 'index.html', {'students': students})

# def detels(request, id):
#     student = get_object_or_404(Student, id=id)
#     return render(request, 'index2.html', {'student': student})

# def update_student(request, id):
#     student = get_object_or_404(Student, id=id)
#     form = StudentModelForm(instance=student)
    
#     if request.method == 'POST':
#         form = StudentModelForm(request.POST, request.FILES, instance=student)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
        

#     return render(request, 'update_student.html', {
#         'student': student,
#         'form': form,
#     })

# def create_student(request):
#     form = StudentModelForm()
#     if request.method == 'POST':
#         form = StudentModelForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
        
#     return render(request, 'create_student.html', {'form': form})

    


# def delete_desert(request, id):
#     desert = get_object_or_404(Student, id=id)
#     desert.delete()
#     return redirect('/')