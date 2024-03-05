from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Group, Student
from .forms import GroupForm, StudentForm

# Create your views here.
def index(request):
    groups = Group.objects.all()
    students = Student.objects.all()
    return render(request, 'index.html', {'groups': groups, 'students': students})

def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('crud:index'))
    else:
        form = GroupForm()

    return render(request, 'form_group.html', {'form': form})

def update_group(request, id):
    group = get_object_or_404(Group, pk=id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect(reverse('crud:index'))
    else:
        form = GroupForm(instance=group)

    return render(request, 'form_group.html', {'form': form})

def delete_group(request, id):
    group = get_object_or_404(Group, pk=id)
    group.delete()
    return redirect(reverse('crud:index'))

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('crud:index'))
    else:
        form = StudentForm()

    return render(request, 'form_student.html', {'form': form})

def update_student(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect(reverse('crud:index'))
    else:
        form = StudentForm(instance=student)

    return render(request, 'form_student.html', {'form': form})

def delete_student(request, id):
    student = get_object_or_404(Student, pk=id)
    student.delete()
    return redirect(reverse('crud:index'))

