from django.urls import path
from .import views_course, views_discipline, views_student, views_home

urlpatterns = [
    path('course/view', views_course.course_list, name='course_list'),
    path('course/new', views_course.course_create, name='course_create'),
    path('course/view/<int:pk>', views_course.course_view, name='course_detail'),
    path('course/edit/<int:pk>', views_course.course_edit, name='course_edit'),
    path('course/delete/<int:pk>', views_course.course_delete, name='course_delete'),

    path('discipline/view', views_discipline.discipline_list, name='discipline_list'),
    path('discipline/new', views_discipline.discipline_create, name='discipline_create'),
    path('discipline/edit/<int:pk>', views_discipline.discipline_edit, name='discipline_edit'),
    path('discipline/delete/<int:pk>', views_discipline.discipline_delete, name='discipline_delete'),

    path('student/view', views_student.student_list, name='student_list'),
    path('student/new', views_student.student_create, name='student_create'),
    path('student/edit/<int:pk>', views_student.student_edit, name='student_edit'),
    path('student/delete/<int:pk>', views_student.student_delete, name='student_delete'),
    path('student/disciplines/<int:pk>', views_student.RegisterStudentInDiscipline, name='student_disciplines'),

    path('relat/disciplines_in_course', views_discipline.RelatDisciplinesInCourse, name='relat_disciplines_in_course'),
    path('relat/students_in_discipline', views_student.RelatStudentsInDiscipline, name='relat_students_in_discipline'),
    path('relat/students_in_course', views_student.RelatStudentsInCourse, name='relat_students_in_course'),

    path('', views_home.home_page, name='home_page'),
]
