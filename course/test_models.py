""" Tests for Course App Models
"""
#pylint: disable=missing-function-docstring

from django.test import TestCase
from .models import Discipline, Course



class DisciplineTests(TestCase):
    """ Test class for Discipline model
    """

    def setUp(self) -> None:
        Discipline.objects.create(discipline='Biologie')
        Discipline.objects.create(discipline='Circus')
        Course.objects.create(discipline=Discipline.objects.get(discipline='Biologie'))

    def test_get_course_count_returns_zero(self):
        self.assertEqual(Discipline.objects.get(discipline='Circus').get_course_count(), 0)

    def test_get_course_count_returns_non_zero(self):
        self.assertEqual(Discipline.objects.get(discipline='Biologie').get_course_count(), 1)

    def test_get_course_count_returns_does_not_exist_exception(self):
        with self.assertRaises(Discipline.DoesNotExist):
            Discipline.objects.get(discipline='FakeDiscipline').get_course_count()
