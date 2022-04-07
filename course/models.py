""" Models for course app
"""
import logging
from django.db import models
from django.contrib import admin

logger = logging.getLogger(__name__)

class Discipline(models.Model):
    """ Discipline model
    """
    discipline = models.CharField(
        'Name of the discipline', max_length=50, unique=True)

    @admin.display(
        description='Number of Courses',
    )
    def get_course_count(self) -> int:
        """ Get number of courses in a discipline
        Returns:
            int: course count
        """
        return Course.objects.filter(discipline=self).count()


    def __str__(self) -> str:
        return f"{self.discipline}"


class Unit(models.Model):
    """ Unit model
    """
    title = models.CharField('Class title', max_length=300, unique=True)
    short_description = models.CharField(
        'Short description of the Class', max_length=500, null=True, blank=True)
    long_description = models.TextField(
        'Long description of the Class', null=True, blank=True)
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def set_active(self) -> bool:
        """ Set's a unit to be active

        Returns:
            bool: True on success, otherwise False
        """
        logger.info("Setting unit %s as active.", self.title)
        self.is_active = True
        return True

    def __str__(self) -> str:
        return f"{self.title}"


class Course(models.Model):
    """ Course model
    """
    title = models.CharField('Course title', max_length=300, unique=True)
    short_description = models.CharField(
        'Short description of the Course', max_length=500, null=True, blank=True)
    long_description = models.TextField(
        'Long description of the Course', null=True, blank=True)
    discipline = models.ForeignKey(
        Discipline, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=False)
    units = models.ManyToManyField(Unit, through='CourseUnits')
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title}"


class CourseUnits(models.Model):
    """ Model representing many-to-many relationship
        between course model and unit model
    """
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """ CourseUnits meta """
        unique_together = (('unit', 'course'), )
