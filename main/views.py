# from django
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# from packages

# from local
from .models import News, Project, Oportunity


# Create your views here.
def home_view(request):
    """Bosh sahifa"""
    oportunities = Oportunity.objects.all()
    if oportunities.count() > 4:
        oportunities = oportunities[-4:]
    
    context = {
        'active_section': 'home',
        'oportunities': oportunities,
    }
    return render(request, 'index.html', context)


def oportunities_view(request):
    """Imkoniyatlar oynsi"""
    chances = Oportunity.objects.all()
    # making nested list The list which is located inside of main list should include 3 objects
    # because The design of webside requires that. 
    # start handling neset list
    list_chances = []
    triple_chances = []
    steps = 0
    for chance in chances: 
        steps += 1
        triple_chances.append(chance)
        if steps == 3:
            list_chances.append(triple_chances)
            steps = 0
            triple_chances = []
    if triple_chances != []:
        list_chances.append(triple_chances)
    # finish handling nested list
    context = {
        'active_section': 'oportunities',
        'list_chances': list_chances,
    }
    return render(request, 'oportunities1.html', context)

def projects_view(request):
    """Loyihalar oynasi"""
    context = {
        'active_section': 'projects'
    }
    return render(request, 'projects.html', context)


def oportunity_detail(request, pk):
    """Imkoniyatlar haqida batafsil ko'rish
    pk = oportunity_id 
    """
    oportunity = get_object_or_404(Oportunity, id=pk)
    context = {
        'active_section': 'oportunity_detail',
        'oportunity': oportunity,
        }
    return render(request, 'oportunity_detail.html', context)


def best_students_view(request):
    """Iqtidorli talabalar oynasi"""
    context = {
        'active_section': 'best_students'
    }
    return render(request, 'best_students.html', context)


def news_view(request):
    """Yangiliklar oynasi"""
    context = {
        'active_section': 'news'
    }
    return render(request, 'news.html', context)


def contact_view(request):
    context = {
        'active_section': 'contact'
    }
    return render(request, 'contact.html', context)