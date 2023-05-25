# from django
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .models import BestStudent, MediaMembers
from main.utils import get_nested_list_includes_triple_lists
# Create your views here.

@login_required(login_url='login')
def best_students_view(request):
    """Iqtidorli talabalar oynasi"""
    students = BestStudent.objects.all().order_by('-created_at')
    context = {
        'active_section': 'best_students',
        'students_list': get_nested_list_includes_triple_lists(students),
    }
    return render(request, 'best_students.html', context)


@login_required(login_url='login')
def student_detail_view(request, pk:int):
    student = get_object_or_404(BestStudent, id=pk)
    context = {
        'active_section': 'None',
        'student': student,
        }
    return render(request, 'student_detail.html', context)


@login_required(login_url='login')
def media_member_detail_view(request, pk):
    member = get_object_or_404(MediaMembers, id=pk)
    context = {
        'active_section': 'None',
        'member': member,
        }
    return render(request, 'media_member_detail.html', context)