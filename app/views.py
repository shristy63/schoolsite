from django.shortcuts import render,redirect
from .models import *
from .forms import CourseForm

def home(request):
    courses=Course.objects.all() 
    teachers=Teacher.objects.all()

    course_count=Course.objects.count()
    student_count=Student.objects.count()
    teachers_count=Teacher.objects.count()
    classroom_count=Classroom.objects.count()

    context={
        "courses":courses,
        "teachers":teachers,
        "course_count":course_count,
        "student_count":student_count,
        "teachers_count":teachers_count,
        "classroom_count":classroom_count

    }
    return render(request,"app/index.html",context)  


def about(request):
    course_count=Course.objects.count()
    student_count=Student.objects.count()
    teachers_count=Teacher.objects.count()
    classroom_count=Classroom.objects.count()

    context={
        "course_count":course_count,
        "student_count":student_count,
        "teachers_count":teachers_count,
        "classroom_count":classroom_count

    }
    return render(request,"app/about.html",context)  


def course(request):
    context={
        "courses":Course.objects.all(),
        "form":CourseForm()
    }
    return render(request,"app/course.html",context)

def course_delete(request,id):
    course=Course.objects.filter(id=id)
    if course:
        course.first().delete()
    return redirect("course")
    

def course_add(request):
    title=request.POST.get("title")
    description=request.POST.get("description")

    Course.objects.create(title=title,
                         description=description)


    # form=CourseForm(request.POST)
    # form.save()

    return redirect("course")

def course_edit(request,id):
    course=Course.objects.filter(id=id)
    if request.method=="POST":
        course=course.first()
        course.title=request.POST.get("title")
        course.description=request.POST.get("description")
        course.save()
        return redirect("course")
    if course:
        form=CourseForm(instance=course.first())
    context={
        "courses":Course.objects.all(),
        "form":form,
        "course_id":id
    }
    return render(request,"app/course_edit.html",context)