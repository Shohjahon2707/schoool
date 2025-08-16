from django.urls import path
from .views import (
    StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView, StudentDeleteView,
    TeacherListView, TeacherDetailView, TeacherCreateView, TeacherUpdateView, TeacherDeleteView,
    ClassListView, ClassDetailView, ClassCreateView, ClassUpdateView, ClassDeleteView,
    SubjectListView, SubjectDetailView, SubjectCreateView, SubjectUpdateView, SubjectDeleteView,
)

urlpatterns = [
    # Student URLs
    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('students/create/', StudentCreateView.as_view(), name='student_create'),
    path('students/<int:pk>/update/', StudentUpdateView.as_view(), name='student_update'),
    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),

    # Teacher URLs
    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('teachers/create/', TeacherCreateView.as_view(), name='teacher_create'),
    path('teachers/<int:pk>/update/', TeacherUpdateView.as_view(), name='teacher_update'),
    path('teachers/<int:pk>/delete/', TeacherDeleteView.as_view(), name='teacher_delete'),

    # Class URLs
    path('classes/', ClassListView.as_view(), name='class_list'),
    path('classes/<int:pk>/', ClassDetailView.as_view(), name='class_detail'),
    path('classes/create/', ClassCreateView.as_view(), name='class_create'),
    path('classes/<int:pk>/update/', ClassUpdateView.as_view(), name='class_update'),
    path('classes/<int:pk>/delete/', ClassDeleteView.as_view(), name='class_delete'),

    # Subject URLs
    path('subjects/', SubjectListView.as_view(), name='subject_list'),
    path('subjects/<int:pk>/', SubjectDetailView.as_view(), name='subject_detail'),
    path('subjects/create/', SubjectCreateView.as_view(), name='subject_create'),
    path('subjects/<int:pk>/update/', SubjectUpdateView.as_view(), name='subject_update'),
    path('subjects/<int:pk>/delete/', SubjectDeleteView.as_view(), name='subject_delete'),
]
