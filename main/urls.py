from django.urls import path

from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('oportunities/', oportunities_view, name='oportunities'),
    path('oportunity_detail/<int:pk>/', oportunity_detail, name="oportunity_detail"),
    path('projects/', projects_view, name="projects"),
    path('project_detail/<int:pk>/', project_detail, name='project_detail'),
    path('news/', news_view, name='news'),
    path('detail_news/<int:pk>/', detail_news, name='detail_news'),
    path('contact/', contact_view, name='contact'),
]