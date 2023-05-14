from django.forms import ModelForm
from crud.models import Course, Student

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_code', 'course_description', 'course_banner']


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'email', 'course', 'phone', 'city', 'address', 'student_image']