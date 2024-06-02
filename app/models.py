from django.db import models
from django.core.validators import ValidationError,MinValueValidator,MaxValueValidator


class AuditModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class Student(AuditModel):
    GENDER_CHOICES = (("M", "Male"), ("F", "Female"), ("O", "Others"))
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=50,choices=GENDER_CHOICES)
    phone_number=models.CharField(max_length=10)
    classroom = models.ForeignKey(
        "Classroom", on_delete=models.DO_NOTHING, related_name="students"
    )

    class Meta:
        verbose_name="student"
        verbose_name_plural="students"

    def clean(self):
        if len(self.phone_number)<10:
            raise ValidationError("Phone number must be of length 10")

    def __str__(self):
        return self.first_name + " " + self.last_name


class Classroom(AuditModel):
    name = models.CharField(max_length=50)
    duration=models.DurationField(blank=True,null=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    is_married=models.BooleanField()
    salary=models.FloatField()
    phone=models.CharField(max_length=10)
    
    def clean(self):
        if len(self.phone)<10:
            raise ValidationError("Phone number must be of length 10")

    def __str__(self):
        return self.name


class Course(AuditModel):
    title=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    teacher=models.ForeignKey(Teacher,on_delete=models.DO_NOTHING,blank=True,null=True)

    def __str__(self):
        return self.title 


class Employee(AuditModel):
    TYPE=(("Teacher","Teacher"),
    ("Board","Board"),
    ("Labour","Labour"))
    name=models.CharField(max_length=50)
    type=models.CharField(max_length=50,choices=TYPE)
    age=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    is_married=models.BooleanField()
    salary=models.FloatField()
    phone=models.CharField(max_length=10)
    teacher=models.OneToOneField(Teacher,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.name+" "+self.type