from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    initials = models.CharField(max_length=2)
    description = models.TextField()

    def __str__(self):
        return self.name


class Discipline(models.Model):
    name = models.CharField(max_length=100)
    initials = models.CharField(max_length=8)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name


class Student(models.Model):
    registration_number = models.AutoField(primary_key=True)
    registration_date = models.DateField(auto_now_add=True)

    name = models.CharField(max_length=120)
    cpf = models.CharField(max_length=30)
    birthdate = models.DateField()

    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    enrolled_disciplines = models.ManyToManyField(Discipline)

    def __str__(self):
        return self.name


class Matricula(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.discipline + ' -> ' + self.student