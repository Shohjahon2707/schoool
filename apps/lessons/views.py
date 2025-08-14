from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Student, Teacher, Class, Subject


class StudentListView(ListView):
    model = Student

class StudentDetailView(DetailView):
    model = Student

class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('student_list')

class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('student_list')


class TeacherListView(ListView):
    model = Teacher

class TeacherDetailView(DetailView):
    model = Teacher

class TeacherCreateView(CreateView):
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy('teacher_list')

class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy('teacher_list')

class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('teacher_list')

class ClassListView(ListView):
    model = Class

class ClassDetailView(DetailView):
    model = Class

class ClassCreateView(CreateView):
    model = Class
    fields = '__all__'
    success_url = reverse_lazy('class_list')

class ClassUpdateView(UpdateView):
    model = Class
    fields = '__all__'
    success_url = reverse_lazy('class_list')

class ClassDeleteView(DeleteView):
    model = Class
    success_url = reverse_lazy('class_list')

class SubjectListView(ListView):
    model = Subject

class SubjectDetailView(DetailView):
    model = Subject

class SubjectCreateView(CreateView):
    model = Subject
    fields = '__all__'
    success_url = reverse_lazy('subject_list')

class SubjectUpdateView(UpdateView):
    model = Subject
    fields = '__all__'
    success_url = reverse_lazy('subject_list')

class SubjectDeleteView(DeleteView):
    model = Subject
    success_url = reverse_lazy('subject_list')

from .models import Subject
from django.shortcuts import render
def subject_list_view(request):
    # klass = request.GET.get('klass')
    # date = request.GET.get('date')
    subjects = Subject.objects.all()
    return render(request, 'subjects.html', context={'subjects': subjects})
# apps/lessons/views.py
