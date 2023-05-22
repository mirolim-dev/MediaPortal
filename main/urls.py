from django.urls import path

from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('oportunities/', oportunities_view, name='oportunities'),
    path('projects/', projects_view, name="projects"),
    path('oportunity_detail/<int:pk>/', oportunity_detail, name="oportunity_detail"),
    path('best_students/', best_students_view, name='best_students'),
    path('news/', news_view, name='news'),
    path('contact/', contact_view, name='contact'),
]