from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from crud.models import Enrolment


# ---------- CRUD ----------

def enrolment_create(request, template_name='crud/enrolment/enrolment_form.html'):
    context = {}
    return render(request, template_name, context)


def enrolment_view(request, pk, template_name='crud/enrolment/enrolment_detail.html'):
    context = {}
    return render(request, template_name, context)


def enrolment_list(request, template_name='crud/enrolment/enrolment_list.html'):
    context = {}
    return render(request, template_name, context)


def enrolment_edit(request, pk, template_name='crud/enrolment/enrolment_form.html'):
    context = {}
    return render(request, template_name, context)


def enrolment_delete(request, pk, template_name='crud/enrolment/enrolment_confirm_delete.html'):
    context = {}
    return render(request, template_name, context)