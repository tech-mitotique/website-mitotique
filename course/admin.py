""" Admin module for Course app
"""
from django.contrib import admin
from course.models import Discipline, Course, Unit, CourseUnits


class DisciplineAdmin(admin.ModelAdmin):
    """ Discipline Admin
    """
    list_display = ['discipline', 'get_course_count', ]


class CourseUnitsInLine(admin.TabularInline):
    """ Admin class to manage FK between Course and Unit
    """
    model = CourseUnits
    extra = 0


class CourseAdmin(admin.ModelAdmin):
    """ Course Admin
    """
    list_display = ['title', 'created_at', 'updated_at', 'is_active', ]
    list_filter = ['is_active', ]
    search_fields = ['title', ]
    inlines = [CourseUnitsInLine, ]


class UnitAdmin(admin.ModelAdmin):
    """ Unit Admin
    """
    list_display = ['title', 'created_at', 'updated_at', 'is_active', ]
    list_filter = ['is_active', ]
    search_fields = ['title', ]
    inlines = [CourseUnitsInLine, ]


admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Unit, UnitAdmin)
