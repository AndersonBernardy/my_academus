from django.db import models

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
    registration_number = models.AutoField(primary_key=True)
    registration_date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=120)
    cpf = models.CharField(max_length=30, unique=True)
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
            models.UniqueConstraint(fields=['name', 'course'], name='unique_enrollment')
        ]

    def __str__(self):
        return self.name


class DisciplineClass(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField()


class ClassTime(models.Model):
    discipline_class = models.ForeignKey(DisciplineClass, on_delete=models.CASCADE)
    class_datetime = models.DateField()


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    discipline_class = models.ForeignKey(DisciplineClass, on_delete=models.PROTECT)
    enrollment_date = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['discipline_class', 'student'], name='unique_enrollment')
        ]


class PresenceChoice(models.Model):
    short = models.CharField(max_length=10, primary_key=True)
    description = models.CharField(max_length=32)
    
    def __str__(self):
        return self.short

class Frequency(models.Model):
    presence = models.ForeignKey(PresenceChoice, on_delete=models.PROTECT)
    class_time = models.ForeignKey(ClassTime, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['class_time', 'student'], name='unique_frequency')
        ]


class Assessment(models.Model):
    assessment_number = models.IntegerField()
    grade = models.DecimalField(max_digits=5, decimal_places=2)
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['assessment_number', 'enrollment'], name='assessment_enrollment')
        ]