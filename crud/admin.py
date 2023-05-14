from django.contrib import admin
from crud.models import Student, Course

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','firstname', 'lastname', 'email', 'course', 'phone', 'city', 'address', 'student_image']
    search_fields = ['firstname', 'lastname', 'email', 'course', 'phone', 'id']
admin.site.register(Student, StudentAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','course_name', 'course_code', 'course_description', 'course_banner']
    search_fields = ['id','course_name', 'course_code']
admin.site.register(Course, CourseAdmin)