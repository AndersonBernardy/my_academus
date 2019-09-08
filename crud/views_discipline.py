from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from crud.models import Discipline, Course


class DisciplineForm(ModelForm):
    class Meta:
        model = Discipline
        fields = ['name', 'initials', 'description', 'course']

def discipline_list(request, template_name='crud/discipline/discipline_list.html'):
    disciplines = Discipline.objects.all()
    context = {'disciplines': disciplines, 'disciplines_count': disciplines.count()}
    return render(request, template_name, context)


def discipline_create(request, template_name='crud/discipline/discipline_form.html'):
    form = DisciplineForm(request.POST or None)
    courses = Course.objects.all()
    if form.is_valid():
        print(form.fields['course'])
        form.save()
        return redirect('discipline_list')
    context = {'action':'create', 'form':form, 'courses':courses}
    return render(request, template_name, context)


def discipline_edit(request, pk, template_name='crud/discipline/discipline_form.html'):
    discipline = get_object_or_404(Discipline, pk=pk)
    courses = Course.objects.all()
    form = DisciplineForm(request.POST or None, instance=discipline)
    if form.is_valid():
        form.save()
        return redirect('discipline_list')
    context = {'action':'edit', 'form':form, 'courses':courses}
    return render(request, template_name, context)


def discipline_delete(request, pk, template_name='crud/discipline/discipline_confirm_delete.html'):
    discipline = get_object_or_404(Discipline, pk=pk)
    if request.method == 'POST':
        discipline.delete()
        return redirect('discipline_list')
    context = {'action':'delete', 'discipline':discipline}
    return render(request, template_name, context)


def RelatDisciplinesInCourse(request, template_name='crud/discipline/discipline_in_course.html'):
    courses = Course.objects.all()

    if request.method == 'GET':
        context = {'courses':courses, 'course':None, 'disciplines':None}

    if request.method == 'POST':
        course = get_object_or_404(Course, pk=request.POST.get("course"))
        disciplines = course.discipline_set.select_related()
        context = {'courses':courses, 'current_course':course, 'disciplines':disciplines}

    return render(request, template_name, context)


# def discipline_view(request, pk, template_name='crud/discipline/discipline_detail.html'):
#     discipline = get_object_or_404(Discipline, pk=pk)    
#     return render(request, template_name, {'discipline':discipline})