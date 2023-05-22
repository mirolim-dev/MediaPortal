from django.contrib import admin

# from locale
from .models import News, Oportunity, Project
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'uploaded_by', 'get_number_of_views', 'created_at']
    list_editable = ('name', 'uploaded_by',)
    search_fields = ('name', 'uploaded_by',)
admin.site.register(News, NewsAdmin)


class OportunityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'responsible_person', 'created_at']
    list_editable = ('name', 'responsible_person',)
    search_fields = ('name', 'responsible_person',)
admin.site.register(Oportunity, OportunityAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'responsible_person', 'get_number_of_views']
    list_editable = ('name', 'responsible_person',)
    search_fields = ('name', 'responsible_person',)
admin.site.register(Project, ProjectAdmin)