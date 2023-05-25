# from django
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages

# from packages

# from local
from .models import News, Project, Oportunity
from .utils import get_nested_list_includes_triple_lists

from students_and_tuiters.models import MediaMembers
# Create your views here.
@login_required(login_url='login')
def home_view(request):
    """Bosh sahifa"""
    oportunities = Oportunity.objects.all()
    media_members = MediaMembers.objects.all()
    if oportunities.count() > 4:
        oportunities = oportunities[-4:]
    
    context = {
        'active_section': 'home',
        'oportunities': oportunities,
        'media_members': get_nested_list_includes_triple_lists(media_members),
    }
    return render(request, 'index.html', context)


@login_required(login_url='login')
def oportunities_view(request):
    """Imkoniyatlar oynsi"""
    chances = Oportunity.objects.all()
    context = {
        'active_section': 'oportunities',
        'list_chances': get_nested_list_includes_triple_lists(chances),
    }
    return render(request, 'oportunities1.html', context)


@login_required(login_url='login')
def projects_view(request):
    """Loyihalar oynasi"""
    projects = Project.objects.all()    
    context = {
        'active_section': 'projects',
        'projects': get_nested_list_includes_triple_lists(projects),
    }
    return render(request, 'projects.html', context)


@login_required(login_url='login')
def project_detail(request, pk:int):
    user = request.user
    project = get_object_or_404(Project, id=pk)
    if user not in project.viewers.all():
        project.viewers.add(user)
    context = {
        'active_section': 'None',
        'project': project,
    }
    return render(request, 'project_detail.html', context)


@login_required(login_url='login')
def oportunity_detail(request, pk):
    """Imkoniyatlar haqida batafsil ko'rish
    pk = oportunity_id 
    """
    oportunity = get_object_or_404(Oportunity, id=pk)
    context = {
        'active_section': 'None',
        'oportunity': oportunity,
        }
    return render(request, 'oportunity_detail.html', context)


@login_required(login_url='login')
def news_view(request):
    """Yangiliklar oynasi"""
    news = News.objects.all().order_by('-created_at')
    context = {
        'active_section': 'news',
        'news': news,
    }
    return render(request, 'news.html', context)


@login_required(login_url='login')
def detail_news(request, pk:int):
    user = request.user
    news = get_object_or_404(News, id=pk)
    if user not in news.viewers.all():
        news.viewers.add(user)
    context = {
        'active_section': 'None',
        'news': news,
    }
    return render(request, 'news_detail.html', context)


@login_required(login_url='login')
def contact_view(request):
    user = request.user
    if request.POST:
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        subject = "Sender: " + full_name + '|' + f'{email}'
        message = request.POST.get('message')
        try:
            send_mail(subject=subject, message=message, from_email=email, recipient_list=['mirolimcoder@gmail.com'], fail_silently=False)
            # send_mail(subject=subject, message=message, from_email='usmanovsacademy@gmail.com', \
            #     recipient_list=['mirolimcoder@gmail.com'])
            messages.success(request, "Sizning xabaringiz yuborildi.E'tibor uchun rahmat.")
            return redirect('contact')
        except:
            messages.error(request, "Habar Jo'natishda nimadur hato ketti")
    context = {
        'active_section': 'contact'
    }
    return render(request, 'contact.html', context)


@login_required(login_url='login')
def send_message(request, path):
    if path == 'None':
        path = 'home'
    user = request.user
    if request.POST:
        full_name = user.first_name + user.last_name
        email = user.email
        subject = "Sender: " + full_name + '|' + f'{email}'
        message = request.POST.get('user_message')
        try:
            send_mail(subject=subject, message=message, from_email=email, recipient_list=['rnabijonov19@gmail.com'], fail_silently=False)
            messages.success(request, "Sizning xabaringiz yuborildi.E'tibor uchun rahmat.")
            
        except:
            messages.error(request, "Habar Jo'natishda nimadur hato ketti")
    return redirect(path)