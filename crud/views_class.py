from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from crud.models import Class


# ---------- CRUD ----------

def class_create(request, template_name='crud/class/class_form.html'):
    context = {}
    return render(request, template_name, context)


def class_view(request, pk, template_name='crud/class/class_detail.html'):
    context = {}
    return render(request, template_name, context)


def class_list(request, template_name='crud/class/class_list.html'):
    classes = Class.objects.all()
    context = {'classes': classes, 'classes_count': 0 + classes.count()}
    return render(request, template_name, context)


def class_edit(request, pk, template_name='crud/class/class_form.html'):
    context = {}
    return render(request, template_name, context)


def class_delete(request, pk, template_name='crud/class/class_confirm_delete.html'):
    context = {}
    return render(request, template_name, context)