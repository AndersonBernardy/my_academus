from django.urls import path
from .import views_course, views_discipline, views_student, views_home, views_class, views_enrolment

urlpatterns = [
    path('course/new', views_course.course_create, name='course_create'),
    path('course/view', views_course.course_list, name='course_list'),
    path('course/view/<int:pk>', views_course.course_view, name='course_detail'),
    path('course/edit/<int:pk>', views_course.course_edit, name='course_edit'),
    path('course/delete/<int:pk>', views_course.course_delete, name='course_delete'),

    path('discipline/new', views_discipline.discipline_create, name='discipline_create'),
    path('discipline/view', views_discipline.discipline_list, name='discipline_list'),
    path('discipline/view/<int:pk>', views_discipline.discipline_view, name='discipline_detail'),
    path('discipline/edit/<int:pk>', views_discipline.discipline_edit, name='discipline_edit'),
    path('discipline/delete/<int:pk>', views_discipline.discipline_delete, name='discipline_delete'),

    path('student/new', views_student.student_create, name='student_create'),
    path('student/view', views_student.student_list, name='student_list'),
    path('student/view/<int:pk>', views_student.student_view, name='student_detail'),
    path('student/edit/<int:pk>', views_student.student_edit, name='student_edit'),
    path('student/delete/<int:pk>', views_student.student_delete, name='student_delete'),

    path('relat/disciplines_in_course', 
        views_discipline.report_disciplines_in_course, name='relat_disciplines_in_course'),
    path('relat/students_in_discipline', 
        views_student.report_students_in_discipline, name='relat_students_in_discipline'),
    path('relat/students_in_course', 
        views_student.report_students_in_course, name='relat_students_in_course'),

    path('', views_home.home_page, name='home_page'),

    path('class/new', views_class.class_create, name='class_create'),
    path('class/view', views_class.class_list, name='class_list'),
    path('class/view/<int:pk>', views_class.class_view, name='class_detail'),
    path('class/edit/<int:pk>', views_class.class_edit, name='class_edit'),
    path('class/delete/<int:pk>', views_class.class_delete, name='class_delete'),

    path('enrolment/student/<int:pk>', views_enrolment.enrolment_edit, name='enrolment_edit'),

]
