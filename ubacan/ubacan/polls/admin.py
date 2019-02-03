from django.contrib import admin

from .models import Question, Choice, Student, StudentCourse, Course

admin.AdminSite.site_header = "Ubacán Administración"
admin.AdminSite.site_title = "Ubacán | UTFSM"

# admin.site.register(Question)
# admin.site.register(Choice)


class CoursesAdmin(admin.ModelAdmin):
                    list_display = ('name_text', 'description')

admin.site.register(Course,CoursesAdmin)

class StudentsAdmin(admin.ModelAdmin):
                    list_display = ('name', 'hobby','creation_date')

admin.site.register(Student,StudentsAdmin)

def upper_case_name(obj):
                        return ("%s %s" % (obj.course.name_text, obj.course.description)).upper()
upper_case_name.short_description = 'Course Name'

class StudentsCoursesAdmin(admin.ModelAdmin):
                    list_display = ( 'student', upper_case_name, 'grade')


admin.site.register(StudentCourse,StudentsCoursesAdmin)

