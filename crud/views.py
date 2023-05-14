from django.shortcuts import render, get_object_or_404, redirect
from crud.models import Course, Student
from crud.forms import CourseForm, StudentForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def view_courses(request):
    courses = Course.objects.all().order_by('-id')
    return render(request, 'view_courses.html', {'courses': courses,})


@login_required
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'course_detail.html', {'course':course,})


@login_required
def add_new_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            ins = form.save()
            ins.save()
            return redirect('course_detail', ins.pk)
    else:
        form = CourseForm()
    return render(request, 'add_new_course.html', {'form':form,})


@login_required
def edit_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            ins = form.save()
            return redirect('course_detail', ins.pk)
    else:
        form = CourseForm(instance=course)
    return render(request, 'add_new_course.html', {'form':form, 'course':course})


@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view-students')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form,})


@login_required
def view_students(request):
    students = Student.objects.all().order_by('-id')
    return render(request, 'view_students.html', {'students':students,})


@login_required
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            ins = form.save()
            return redirect('edit-student', ins.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'add_student.html', {'form':form, 'student':student})


@login_required
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('view-students')