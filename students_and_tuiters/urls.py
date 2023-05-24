# from django
from django.urls import path

# from local
from .views import best_students_view, student_detail_view, media_member_detail_view
urlpatterns = [
    path('best_students/', best_students_view, name='best_students'),
    path('detail/<int:pk>/', student_detail_view, name="student_detail"),
    path('media_member/detail/<int:pk>/', media_member_detail_view, name="media_member_detail"),
]
