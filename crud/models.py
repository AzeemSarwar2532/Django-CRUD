from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_code = models.CharField(max_length=255)
    course_description = models.TextField()
    course_banner = models.ImageField(upload_to='course_banners/', blank=True)

    def __str__(self):
        return self.course_name
    

class Student(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    student_image = models.ImageField(upload_to='student_images/', blank=True)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname