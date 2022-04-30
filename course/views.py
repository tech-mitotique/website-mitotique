""" Views for course app
"""

from django.views.generic import View, ListView, DetailView
from django.shortcuts import render
from course.models import Course


class HomePage(View):
    """ Home page view """
    def get(self, request):
        """ get method override for homepage view """
        return render(request, 'course/homepage.html')


class CourseListView(ListView):
    """ Generic ListView for Course model """
    model = Course

class CourseDetailView(DetailView):
    """ Generic DetailVire for Course model """
    model = Course
