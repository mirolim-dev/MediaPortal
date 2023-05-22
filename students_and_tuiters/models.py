# from django
from django.db import models
from django.contrib.auth.models import User

# from packages
from ckeditor_uploader.fields import RichTextUploadingField, RichTextUploadingFormField
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# from local
# Create your models here.

class Tuiter(models.Model):
    class Meta:
        verbose_name_plural="Tuiterlar"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=17, verbose_name="Telefon raqami", unique=True)
    image = models.ImageField(upload_to="tuiters/", blank=True, null=True, verbose_name='rasm')
    bio = models.TextField(verbose_name='izoh')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"
    

class BestStudent(models.Model):
    class Meta:
        verbose_name = 'Iqtidorli Talaba'
        verbose_name_plural = "Iqtidorli Talabalar"
    first_name = models.CharField(max_length=30, verbose_name='Ism')
    last_name = models.CharField(max_length=30, verbose_name='Familya')
    group = models.CharField(max_length=10, verbose_name='guruh')
    shortly_description = models.TextField(max_length=250, verbose_name='qisqacha izoh')
    image = models.ImageField(upload_to='students/', verbose_name='rasm')
    description = RichTextUploadingField(verbose_name="Izoh")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


    