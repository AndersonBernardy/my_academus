from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from crud.models import Class, Discipline, Enrolment, Assessment, Grade


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


# ---------- GRADES ----------

class GradeForm(ModelForm):
    class Meta:
        model = Grade
        fields = ['grade']


def grade_list(request, pk, template_name='crud/grades/grade_list.html'):
    enrolment = get_object_or_404(Enrolment, pk=pk)
    assessments = Assessment.objects.filter(d_class=enrolment.d_class)

    for assessment in assessments:
        grade = Grade.objects.filter(assessment=assessment, enrolment=enrolment).first()
        if(grade == None):
            grade = Grade.objects.create(enrolment=enrolment, assessment=assessment, grade=0.0)
        assessment.result = grade

    context = {'action': 'list', 'enrolment': enrolment, 'assessments': assessments}
    return render(request, template_name, context)


def grade_edit(request, pk, template_name='crud/grades/grade_edit.html'):
    grade = get_object_or_404(Grade, pk=pk)
    context = {'action:': 'edit', 'grade': grade}

    for k,v in request.POST.items():
        print(k, v)

    form = GradeForm(request.POST or None, instance=grade)
    if form.is_valid():
        form.save()
        return redirect("grade_list", pk=grade.enrolment.id)

    return render(request, template_name, context)


# ---------- GRADES ----------

def frequency_list(request, pk, template_name='crud/frequency/frequency_list.html'):
    context = {'action': 'list', }
    return render(request, template_name, context)

def frequency_edit(request, pk, template_name='crud/frequency/frequency_edit.html'):
    context = {'action': 'edit', }
    return render(request, template_name, context)