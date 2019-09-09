from django.contrib import admin
from crud.models import Student, Course, Discipline, DurationChoice, PresenceChoice, AcademicPeriod, Class

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Discipline)
admin.site.register(DurationChoice)
admin.site.register(PresenceChoice)
admin.site.register(AcademicPeriod)
admin.site.register(Class)