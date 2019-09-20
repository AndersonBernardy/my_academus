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

    if request.method == 'POST':
        persisted_classes = set(d_class.code for d_class in student.persisted_classes)
        selected_classes =  set(request.POST.getlist('d_class_code[]'))
        classes_to_remove = persisted_classes - selected_classes
        classes_to_add = selected_classes - persisted_classes

        for code in classes_to_add:
            d_class = Class.objects.filter(code=code).first()
            Enrolment.objects.create(student=student, d_class=d_class)

        for code in classes_to_remove:
            d_class = Class.objects.filter(code=code).first()
            Enrolment.objects.filter(d_class=d_class, student=student).delete()

        return redirect('student_list')

    available_classes = set(Class.objects.filter(discipline__course__id=student.course.id)) - set(student.persisted_classes)
    context = {'action':'edit', 'student': student, 'available_classes': available_classes}
    return render(request, template_name, context)