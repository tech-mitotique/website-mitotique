""" URLs for course app """

from django.urls import path
from course import views

app_name = 'course'
urlpatterns = [
    path('', views.HomePage.as_view(), name='Homepage'),
    path('courses/', views.CourseListView.as_view(), name='CourseList'),
    path('course/<int:course_id>', views.CourseDetailView.as_view(), name='CourseDetails'),
]
