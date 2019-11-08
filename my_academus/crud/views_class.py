from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
import calendar
import datetime

from crud.models import Class, Discipline, Enrolment, Assessment, Grade, ClassTime, Frequency, PresenceChoice


class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields = ['code', 'discipline', 'start_date', 'end_date']


# ---------- CRUD ----------

def class_create(request, template_name='crud/class/class_form.html'):

    form = ClassForm(request.POST or None)
    if form.is_valid():
        d_class = form.save()

        for assessment_name in filter(None, request.POST.getlist('assessment[]')):
            Assessment.objects.create(assessment_name=assessment_name, d_class=d_class)

        class_week = [int(week_day) for week_day in request.POST.getlist('class_week[]')]
        class_time = [datetime.datetime.strptime(time, "%H:%M") for time in request.POST.getlist('class_time[]')]

        for year in range(d_class.start_date.year, d_class.end_date.year + 1):
            for month in range(d_class.start_date.month, d_class.end_date.month + 1):
                cal = calendar.monthcalendar(year, month)
                for week in cal:
                    for week_day, time in zip(class_week, class_time):
                        if(week[week_day]) != 0:
                            class_datetime = datetime.datetime(year, month, week[week_day], time.hour, time.minute, time.second)
                            d = datetime.date(year, month, week[week_day])
                            if d > d_class.start_date and d < d_class.end_date:
                                ClassTime.objects.create(class_datetime=class_datetime, d_class=d_class)

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
    d_class = get_object_or_404(Class, pk=pk)
    start_date = d_class.start_date.strftime('%Y-%m-%d')
    end_date = d_class.end_date.strftime('%Y-%m-%d')

    form = ClassForm(request.POST or None, instance=d_class)
    if form.is_valid():
        form.save()
        return redirect('class_list')

    disciplines = Discipline.objects.all()
    context = {'action':'edit', 'form':form, 'disciplines':disciplines, 'start_date': start_date, 'end_date': end_date}
    return render(request, template_name, context)


def class_delete(request, pk, template_name='crud/class/class_confirm_delete.html'):
    d_class = get_object_or_404(Class, pk=pk)
    if request.method == 'POST':
        d_class.delete()
        return redirect('class_list')
    context = {'action': 'delete', 'd_class': d_class}
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

    form = GradeForm(request.POST or None, instance=grade)
    if form.is_valid():
        form.save()
        return redirect("grade_list", pk=grade.enrolment.id)

    return render(request, template_name, context)


# ---------- FREQUENCY ----------

class FrequencyForm(ModelForm):
    class Meta:
        model = Frequency
        fields = ['presence']


def frequency_list(request, pk, template_name='crud/frequency/frequency_list.html'):
    enrolment = get_object_or_404(Enrolment, pk=pk)
    class_times = ClassTime.objects.filter(d_class=enrolment.d_class)

    for class_time in class_times:
        frequency = Frequency.objects.filter(class_time=class_time, enrolment=enrolment).first()
        if(frequency == None):
            presence = PresenceChoice.objects.filter(short="*").first()
            frequency = Frequency.objects.create(class_time=class_time, enrolment=enrolment, presence=presence)
        class_time.frequency = frequency

    context = {'action': 'list', 'enrolment': enrolment, 'class_times': class_times}
    return render(request, template_name, context)


def frequency_edit(request, pk, template_name='crud/frequency/frequency_edit.html'):
    frequency = get_object_or_404(Frequency, pk=pk)
    presence_choices = PresenceChoice.objects.all()
    form = FrequencyForm(request.POST or None, instance=frequency)

    if form.is_valid():
        form.save()
        return redirect("frequency_list", pk=frequency.enrolment.id)

    context = {'action:': 'edit', 'frequency': frequency, 'presence_choices': presence_choices, 'form': form}
    return render(request, template_name, context)