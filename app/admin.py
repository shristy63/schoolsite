from django.contrib import admin
from .models import *

admin.site.register(Student)

class CourseInline(admin.StackedInline):
    verbose_name="Taught Course"
    model=Course
    extra=1 

class TeacherAdmin(admin.ModelAdmin):
    list_per_page=10 
    inlines=[CourseInline]
    list_display=['name','age','salary']
    list_filter=('name','age')

    def get_readonly_fields(self, request, obj=None):
        return ("age",) 


admin.site.register(Teacher,TeacherAdmin)

class ClassroomAdmin(admin.ModelAdmin):
    list_display=['id','name']
admin.site.register(Classroom,ClassroomAdmin)

admin.site.register(Employee)
admin.site.register(Course)


admin.site.site_header = "School Site"
admin.site.site_title = "School Site title"