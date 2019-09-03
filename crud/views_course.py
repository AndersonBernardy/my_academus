from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from crud.models import Course


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'initials']


def course_list(request, template_name='crud/course/course_list.html'):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, template_name, context)


def course_create(request, template_name='crud/course/course_form.html'):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('course_list')
    context = {'action':'create', 'form':form}
    return render(request, template_name, context)


def course_edit(request, pk, template_name='crud/course/course_form.html'):
    course = get_object_or_404(Course, pk=pk)
    form = CourseForm(request.POST or None, instance=course)
    if form.is_valid():
        form.save()
        return redirect('course_list')
    context = {'action':'edit', 'form':form}
    return render(request, template_name, context)


def course_delete(request, pk, template_name='crud/course/course_confirm_delete.html'):
    course = get_object_or_404(Course, pk=pk)
    if request.method=='POST':
        course.delete()
        return redirect('course_list')
    context = {'action':'delete', 'course':course}
    return render(request, template_name, context)


# def course_view(request, pk, template_name='crud/course/course_detail.html'):
#     course = get_object_or_404(Course, pk=pk)
#     context = {'action':'list', 'course': course}
#     return render(request, template_name, context)