from django.db import models

class courses(models.Model):
    CourseName=models.CharField(max_length=50)
    CourseId=models.IntegerField(default=5,primary_key=True)
    CourseFee=models.IntegerField(default=5)
    CourseDuration=models.IntegerField(default=3)
class faculity(models.Model):
    id=models.IntegerField(default=4,primary_key=True)
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    cno=models.IntegerField(default=10)
    course=models.CharField(max_length=30)
    exp=models.DecimalField(max_digits=2,decimal_places=1)

class student(models.Model):
    name=models.CharField(max_length=50)
    cno=models.IntegerField(default=10,primary_key=True)
    gender=models.CharField(max_length=10)
    username=models.CharField(max_length=50)
    password=models.IntegerField(default=10)
    email=models.EmailField()

class companyregister(models.Model):
    c_id=models.IntegerField(default=10,primary_key=True)
    c_name=models.CharField(max_length=50)
    c_hrname=models.CharField(max_length=50)
    c_email=models.EmailField()
    c_contact=models.IntegerField(default=10)
    c_purpose=models.CharField(max_length=50)
    c_address=models.CharField(max_length=100)
    c_status=models.CharField(max_length=30)

