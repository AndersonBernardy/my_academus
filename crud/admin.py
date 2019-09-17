from django.contrib import admin
from crud.models import Student, Course, Discipline, DurationChoice, PresenceChoice, AcademicPeriod, Class, Enrolment, Assessment, Grade, ClassTime, Frequency

admin.site.register(DurationChoice)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(AcademicPeriod)
admin.site.register(Discipline)
admin.site.register(Class)
admin.site.register(ClassTime)
admin.site.register(Enrolment)
admin.site.register(PresenceChoice)
admin.site.register(Frequency)
admin.site.register(Assessment)
admin.site.register(Grade)