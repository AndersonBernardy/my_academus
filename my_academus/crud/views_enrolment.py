from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from crud.models import Enrolment, Student, Class, Course


class EnrolmentForm(ModelForm):
    class Meta:
        model = Enrolment
        fields = ['student', 'd_class']


# ---------- CRUD ----------




def enrolment_edit(request, pk, template_name='crud/enrolment/enrolment_form.html'):
    student = get_object_or_404(Student, pk=pk)
    student.persisted_classes = [enrolment.d_class for enrolment in student.enrolment_set.select_related()]
    print(student.persisted_classes)

    if request.method == 'POST':
        selected_classes = request.POST.getlist('selected_classes')

    # form = EnrolmentForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #     return redirect('home_page')

    classes = Class.objects.filter(discipline__course__id = student.course.id)
    context = {'action':'edit', 'student': student, 'classes': classes}
    return render(request, template_name, context)