from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import FileSystemStorage
from studens.models import Student, Group
from .forms import StudentModelForm, StudentForm
from .filters import StudentFilter

def main(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})

def detels(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'index2.html', {'student': student})

def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentModelForm(instance=student)
    
    if request.method == 'POST':
        form = StudentModelForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/')
        

    return render(request, 'update_student.html', {
        'student': student,
        'form': form,
    })

def create_student(request):
    form = StudentModelForm()
    if request.method == 'POST':
        form = StudentModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    return render(request, 'create_student.html', {'form': form})

    


def delete_desert(request, id):
    desert = get_object_or_404(Student, id=id)
    desert.delete()
    return redirect('/')