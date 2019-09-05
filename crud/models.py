from django.db import models


class Course(models.Model):
    DURATION_YEAR_CHOICES = [
        ("one_year", '1 Ano'),
        ("two_years", '2 Anos'),
        ("three_years", '3 Anos'),
        ("four_years", '4 Anos'),
        ("five_years", '5 Anos'),
        ("six_years", '6 Anos'),
    ]

    name = models.CharField(max_length=100, unique=True)
    initials = models.CharField(max_length=8, unique=True)
    description = models.TextField()
    duration_years = models.CharField(max_length=8, choices=DURATION_YEAR_CHOICES)

    def __str__(self):
        return self.name


class Student(models.Model):
    registration_number = models.AutoField(primary_key=True)
    registration_date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=120)
    cpf = models.CharField(max_length=30, unique=True)
    birthdate = models.DateField()

    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Discipline(models.Model):
    name = models.CharField(max_length=100, unique=True)
    initials = models.CharField(max_length=8)
    description = models.TextField()
    academic_period = models.CharField(max_length=16)

    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class DisciplineClass(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()


class ClassTime(models.Model):
    discipline_class = models.ForeignKey(DisciplineClass, on_delete=models.CASCADE)
    class_datetime = models.DateField()


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    discipline_class = models.ForeignKey(DisciplineClass, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['discipline_class', 'student'], name='unique_enrollment')
        ]


class Frequency(models.Model):
    PRESENCE_CHOICES = [
        ("not_informed", ""),
        ("present", "P"),
        ("absence", "F"),
    ]

    presence = models.CharField(max_length=16, choices=PRESENCE_CHOICES)
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