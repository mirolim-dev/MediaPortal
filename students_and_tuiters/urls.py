# from django
from django.urls import path

# from local
from .views import best_students_view, student_detail_view
urlpatterns = [
    path('best_students/', best_students_view, name='best_students'),
    path('detail/<int:pk>/', student_detail_view, name="student_detail"),
]
