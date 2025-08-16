from django.contrib import admin
from apps.lessons.models import Subject, Teacher, Class, Student

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')
    filter_horizontal = ('subject',)  # Чтобы выбирать предметы через удобный интерфейс


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'capacity', 'major', 'curator', 'room_number', 'created_at')
    search_fields = ('name', 'major', 'room_number')
    list_filter = ('major', 'curator')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')

