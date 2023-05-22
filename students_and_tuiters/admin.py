from django.contrib import admin


# from models
from .models import Tuiter, BestStudent

# Register your models here.

class TuiterAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'created_at']
    list_editable = ('phone',)
    search_fields = ('phone',)
admin.site.register(Tuiter, TuiterAdmin)


class BestStudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'group', 'created_at']
    list_editable = ('first_name', 'last_name', 'group')
    search_fields = ('first_name', 'last_name', 'group',)
admin.site.register(BestStudent, BestStudentAdmin)