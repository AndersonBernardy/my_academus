from django.db import models
from django.core.exceptions import ValidationError


class DurationChoice(models.Model):
    short = models.CharField(max_length=10, primary_key=True)
    description = models.CharField(max_length=32)

    def __str__(self):
        return self.description


class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    initials = models.CharField(max_length=8, unique=True)
    description = models.TextField()
    duration = models.ForeignKey(DurationChoice, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Student(models.Model):
    def validate_cpf(cpf):
        if len(cpf) < 11 or len(cpf) > 14:
            raise ValidationError("CPF inválido: %s".format(cpf))
        return True

    registration_number = models.AutoField(primary_key=True)
    registration_date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=120)
    cpf = models.CharField(max_length=30, unique=True, validators=[validate_cpf])
    birthdate = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class AcademicPeriod(models.Model):
    short = models.CharField(max_length=10, primary_key=True)
    description = models.CharField(max_length=32)

    def __str__(self):
        return self.description


class Discipline(models.Model):
    name = models.CharField(max_length=100)
    initials = models.CharField(max_length=8)
    description = models.TextField()
    academic_period = models.ForeignKey(AcademicPeriod, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'course'], name='unique_discipline_name'),
            models.UniqueConstraint(fields=['initials', 'course'], name='unique_discipline_initials'),
        ]

    def __str__(self):
        return self.course.initials + " - " + self.name


class Class(models.Model):
    code = models.CharField(max_length=16, unique=True)
    discipline = models.ForeignKey(Discipline, on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.code


class ClassTime(models.Model):
    d_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    class_datetime = models.DateField()


class Enrolment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    d_class = models.ForeignKey(Class, on_delete=models.PROTECT)
    enrolment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.student.name + " (" + self.d_class.code + ")"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['d_class', 'student'], name='unique_enrolment')
        ]


class PresenceChoice(models.Model):
    short = models.CharField(max_length=10, primary_key=True)
    description = models.CharField(max_length=32)
    
    def __str__(self):
        return self.short


class Frequency(models.Model):
    presence = models.ForeignKey(PresenceChoice, on_delete=models.PROTECT)
    class_time = models.ForeignKey(ClassTime, on_delete=models.CASCADE)
    enrolment = models.ForeignKey(Enrolment, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['class_time', 'enrolment'], name='unique_frequency')
        ]


class Assessment(models.Model):
    assessment_name = models.CharField(max_length=32)
    d_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.assessment_name + " (" + self.d_class.code + ")"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['assessment_name', 'd_class'], name='assessment_class')
        ]


class Grade(models.Model):
    def validate_grade(grade):
        if(grade < 0 or grade > 100):
            raise ValidationError("Nota inválida: %d".format(grade))
        return True

    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='grade_set')
    grade = models.DecimalField(max_digits=4, decimal_places=1, validators=[validate_grade])
    enrolment = models.ForeignKey(Enrolment, on_delete=models.CASCADE, related_name='grade_set')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['assessment', 'enrolment'], name='assessment_enrolment')
        ]