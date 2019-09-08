from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm

from crud.models import Student, Discipline, Course


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'birthdate', 'cpf', 'course',]


def student_list(request, template_name='crud/student/student_list.html'):
    students = Student.objects.all()
    context = {'students': students, 'students_count': students.count()}
    return render(request, template_name, context)


def student_create(request, template_name='crud/student/student_form.html'):
    form = StudentForm(request.POST or None)
    courses = Course.objects.all()
    if form.is_valid():
        form.save()
        return redirect('student_list')
    context = {'action':'create', 'form':form, 'courses':courses}
    return render(request, template_name, context)


def student_edit(request, pk, template_name='crud/student/student_form.html'):
    student = get_object_or_404(Student, pk=pk)
    courses = Course.objects.all()
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    birthdate = student.birthdate.strftime('%Y-%m-%d')
    context = {'action':'edit', 'form':form, 'courses':courses, 'birthdate':birthdate}
    return render(request, template_name, context)


def student_delete(request, pk, template_name='crud/student/student_confirm_delete.html'):
    student = get_object_or_404(Student, pk=pk)
    if request.method=='POST':
        student.delete()
        return redirect('student_list')
    context = {'action':'delete', 'student':student}
    return render(request, template_name, context)


def RelatStudentsInDiscipline(request, template_name='crud/student/student_in_discipline.html'):
    disciplines = Discipline.objects.all()

    if request.method == 'GET':
        context = {'disciplines':disciplines, 'discipline':None, 'students':None}

    if request.method == 'POST':
        discipline = get_object_or_404(Discipline, pk=request.POST.get("discipline"))
        students = discipline.student_set.select_related()
        context = {'disciplines':disciplines, 'current_discipline':discipline, 'students':students}

    return render(request, template_name, context)


def RelatStudentsInCourse(request, template_name='crud/student/student_in_course.html'):
    courses = Course.objects.all()

    if request.method == 'GET':
        context = {'courses':courses, 'course':None, 'disciplines':None}

    if request.method == 'POST':
        course = get_object_or_404(Course, pk=request.POST.get("course"))
        students = course.student_set.select_related()
        context = {'courses':courses, 'current_course':course, 'students':students}

    return render(request, template_name, context)

def RegisterStudentInDiscipline(request, pk, template_name="crud/student/student_disciplines.html"):
    student = get_object_or_404(Student, pk=pk)
    disciplines = Discipline.objects.filter(course=student.course)
    enrolled_disciplines = student.enrolled_disciplines.all()
    context = {
        'student':student,
        'disciplines':disciplines,
        'enrolled_disciplines':enrolled_disciplines
    }

    if request.method == 'POST':
        if request.POST.get('disciplines') != None:
            student.enrolled_disciplines.set(request.POST.getlist('disciplines'))
            student.save()

    return render(request, template_name, context)
