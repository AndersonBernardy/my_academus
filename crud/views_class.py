from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from crud.models import Class, Discipline

class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields = ['code', 'discipline', 'start_date', 'end_date']



# ---------- CRUD ----------

def class_create(request, template_name='crud/class/class_form.html'):
    form = ClassForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('class_list')
        
    disciplines = Discipline.objects.all()
    context = {'action':'create', 'form':form, 'disciplines':disciplines}
    return render(request, template_name, context)


def class_view(request, pk, template_name='crud/class/class_detail.html'):
    d_class = get_object_or_404(Class, pk=pk)
    d_class.start_date = d_class.start_date.strftime('%Y-%m-%d')
    d_class.end_date = d_class.end_date.strftime('%Y-%m-%d')
    enrolments = d_class.enrolment_set.select_related()
    enrolments.count = 0 + enrolments.count()
    context = {'action': 'view', 'd_class': d_class, 'enrolments': enrolments}
    return render(request, template_name, context)


def class_list(request, template_name='crud/class/class_list.html'):
    classes = Class.objects.all()
    classes.count = 0 + classes.count()
    context = {'action': 'list', 'classes': classes}
    return render(request, template_name, context)


def class_edit(request, pk, template_name='crud/class/class_form.html'):
    context = {'action': 'edit', }
    return render(request, template_name, context)


def class_delete(request, pk, template_name='crud/class/class_confirm_delete.html'):
    context = {'action': 'delete', }
    return render(request, template_name, context)