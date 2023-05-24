# from django
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# from packages
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# from local

# Create your models here.

class News(models.Model):
    """Tuiterlarham qo'shaolsin"""
    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = "Yangiliklar"
    name = models.CharField(max_length=80, verbose_name='nomi')
    shortly_description = models.TextField(max_length=200, verbose_name='qisqacha izoh')
    image = models.ImageField(upload_to='news/', verbose_name="rasm")
    description = RichTextUploadingField(verbose_name="Izoh")
    uploaded_by = models.CharField(max_length=60, verbose_name="Yuklovchi shaxs")
    viewers = models.ManyToManyField(User, blank=True, verbose_name="Ko'ruvchilar")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
    
    @admin.display(description="Ko'rishlar soni")
    def get_number_of_views(self):
        return self.viewers.count()


class Oportunity(models.Model): #Faqat super user qo'shsin
    """Only Super user can add this"""
    class Meta:
        verbose_name = 'Imkoniyat'
        verbose_name_plural = "Imkoniyatlar"
    name = models.CharField(max_length=80, verbose_name="nomi")
    shortly_description = models.TextField(max_length=200, verbose_name='qisqacha izoh')
    image = models.ImageField(upload_to="chances/", verbose_name="rasm")
    responsible_person = models.CharField(max_length=60, verbose_name="Masul shaxs")
    description = RichTextUploadingField(verbose_name="Izoh")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    

class Project(models.Model): #Tuiterlar ham buni qo'shaolsin
    """Tuiters can add this as well"""
    class Meta:
        verbose_name = 'Loyiha'
        verbose_name_plural = 'Loyihalar'
    name = models.CharField(max_length=60, verbose_name='nomi')
    shortly_description = models.TextField(max_length=200, verbose_name='qisqacha izoh')
    image = models.ImageField(upload_to="chances/", verbose_name="rasm")
    responsible_person = models.CharField(max_length=60, verbose_name="Masul shaxs")
    description = RichTextUploadingField(verbose_name="Izoh")
    viewers = models.ManyToManyField(User, blank=True, verbose_name="Ko'ruvchilar")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    @admin.display(description="Ko'rishlar soni")
    def get_number_of_views(self):
        return self.viewers.count()