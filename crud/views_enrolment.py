from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from crud.models import Enrolment, Student, Class


class EnrolmentForm(ModelForm):
    class Meta:
        model = Enrolment
        fields = ['student', 'd_class']


# ---------- CRUD ----------

def enrolment_create(request, template_name='crud/enrolment/enrolment_form.html'):
    form = EnrolmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home_page')

    students = Student.objects.all()
    classes = Class.objects.all()
    context = {'action':'create', 'students': students, 'classes': classes}
    return render(request, template_name, context)


def enrolment_view(request, pk, template_name='crud/enrolment/enrolment_detail.html'):
    context = {'action':'view', }
    return render(request, template_name, context)


def enrolment_list(request, template_name='crud/enrolment/enrolment_list.html'):
    context = {'action':'list', }
    return render(request, template_name, context)


def enrolment_edit(request, pk, template_name='crud/enrolment/enrolment_form.html'):
    context = {'action':'edit', }
    return render(request, template_name, context)


def enrolment_delete(request, pk, template_name='crud/enrolment/enrolment_confirm_delete.html'):
    context = {'action':'delete', }
    return render(request, template_name, context)