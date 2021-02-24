from django.db import models


class Group(models.Model):
    group_number = models.CharField(max_length=20)
    logo_group = models.ImageField()
    group_description = models.TextField()

    def __str__(self):
        return self.group_number


class Student(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    student_photo = models.ImageField()
    student_number = models.CharField(max_length=50)
    firstname_student = models.CharField(max_length=20)
    lastname_student = models.CharField(max_length=20, null=True, blank=True)  # делает вводимое поле необязательным
    description = models.TextField()

    def __str__(self):
        return self.student_number


class Work(models.Model):
    students = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    works_description = models.TextField()

    def __str__(self):
        return self.title
