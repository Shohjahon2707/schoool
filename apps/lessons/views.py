from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Student, Teacher, Class, Subject
from datetime import datetime

# --------------------------
# HOME
# --------------------------
def home_view(request):
    return render(request, 'home.html', {'year': datetime.now().year})

# --------------------------
# UNIVERSAL CRUD VIEWS
# --------------------------

# STUDENT
class StudentListView(ListView):
    model = Student
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Student'
        context['create_url'] = reverse_lazy('student_create')
        return context

class StudentDetailView(DetailView):
    model = Student
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Student'
        context['update_url'] = reverse_lazy('student_update', kwargs={'pk': self.object.pk})
        context['delete_url'] = reverse_lazy('student_delete', kwargs={'pk': self.object.pk})
        context['fields'] = [
            ('First name', self.object.first_name),
            ('Last name', self.object.last_name),
            ('Email', self.object.email),
            ('Phone', self.object.phone_number),
            ('Photo', self.object.pfp.url if self.object.pfp else None),
        ]
        return context


class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('student_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Student'
        context['cancel_url'] = reverse_lazy('student_list')
        return context

class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('student_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Student'
        context['cancel_url'] = reverse_lazy('student_list')
        return context

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('student_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Student'
        context['cancel_url'] = reverse_lazy('student_list')
        return context

# TEACHER
class TeacherListView(ListView):
    model = Teacher
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Teacher'
        context['create_url'] = reverse_lazy('teacher_create')
        return context

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Teacher'
        context['update_url'] = reverse_lazy('teacher_update', kwargs={'pk': self.object.pk})
        context['delete_url'] = reverse_lazy('teacher_delete', kwargs={'pk': self.object.pk})
        context['fields'] = [
            ('First name', self.object.first_name),
            ('Last name', self.object.last_name),
            ('Email', self.object.email),
            ('Phone', self.object.phone_number),
            ('Photo', self.object.pfp.url if self.object.pfp else None),
            ('Subjects', ', '.join([subject.name for subject in self.object.subject.all()])),
        ]
        return context

class TeacherCreateView(CreateView):
    model = Teacher
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('teacher_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Teacher'
        context['cancel_url'] = reverse_lazy('teacher_list')
        return context

class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('teacher_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Teacher'
        context['cancel_url'] = reverse_lazy('teacher_list')
        return context

class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('teacher_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Teacher'
        context['cancel_url'] = reverse_lazy('teacher_list')
        return context

# CLASS
class ClassListView(ListView):
    model = Class
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Class'
        context['create_url'] = reverse_lazy('class_create')
        return context

class ClassDetailView(DetailView):
    model = Class
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Class'
        context['update_url'] = reverse_lazy('class_update', kwargs={'pk': self.object.pk})
        context['delete_url'] = reverse_lazy('class_delete', kwargs={'pk': self.object.pk})
        context['fields'] = [
            ('Name', self.object.name),
            ('Capacity', self.object.capacity),
            ('Major', self.object.major),
            ('Curator', f'{self.object.curator.first_name} {self.object.curator.last_name}'),
            ('Room Number', self.object.room_number),
        ]
        return context

class ClassCreateView(CreateView):
    model = Class
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('class_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Class'
        context['cancel_url'] = reverse_lazy('class_list')
        return context

class ClassUpdateView(UpdateView):
    model = Class
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('class_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Class'
        context['cancel_url'] = reverse_lazy('class_list')
        return context

class ClassDeleteView(DeleteView):
    model = Class
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('class_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Class'
        context['cancel_url'] = reverse_lazy('class_list')
        return context

# SUBJECT
class SubjectListView(ListView):
    model = Subject
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Subject'
        context['create_url'] = reverse_lazy('subject_create')
        return context

class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Subject'
        context['update_url'] = reverse_lazy('subject_update', kwargs={'pk': self.object.pk})
        context['delete_url'] = reverse_lazy('subject_delete', kwargs={'pk': self.object.pk})
        context['fields'] = [
            ('Name', self.object.name),
        ]
        return context


class SubjectCreateView(CreateView):
    model = Subject
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('subject_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Subject'
        context['cancel_url'] = reverse_lazy('subject_list')
        return context

class SubjectUpdateView(UpdateView):
    model = Subject
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('subject_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Subject'
        context['cancel_url'] = reverse_lazy('subject_list')
        return context

class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('subject_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Subject'
        context['cancel_url'] = reverse_lazy('subject_list')
        return context
