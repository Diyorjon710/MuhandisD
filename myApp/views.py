from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import CarouselModel, NewsModel, ProjectsCategoryModel, ProjectsModel, ProjectVideosModel, StudentsModel, PartnersModel

def homePageViewUZ(request):
    carousel_first = CarouselModel.objects.all()[:1]
    carousel = CarouselModel.objects.all()[1:]
    news = NewsModel.objects.all().order_by('-id')[:3]
    projects_category = ProjectsCategoryModel.objects.all()
    project_videos = ProjectVideosModel.objects.all().order_by('-id')[:3]
    students = StudentsModel.objects.all()[:4]
    partners = PartnersModel.objects.all()

    context = {
        'carousel_first': carousel_first,
        'carousel': carousel,
        'news': news,
        'projects_category': projects_category,
        'project_videos': project_videos,
        'students': students,
        'partners': partners
    }

    return render(request, 'uz/index_uz.html', context)

class OneNewsViewUZ(DetailView):
    model = NewsModel
    template_name = 'uz/oneNews_uz.html'

def allNewsViewUZ(request):
    all_news = NewsModel.objects.all().order_by('-id')

    context = {
        'all_news': all_news
    }

    return render(request, 'uz/allNews_uz.html', context)

def allProjectsViewUZ(request, pk):
    allProjects = ProjectsModel.objects.all().filter(project_category=pk)

    context = {
        'allProjects': allProjects
    }

    return render(request, 'uz/allProjects_uz.html', context)

class OneProjectViewUZ(DetailView):
    model = ProjectsModel
    template_name = 'uz/oneProject_uz.html'

class AllVideosViewUZ(ListView):
    model = ProjectVideosModel
    template_name = 'uz/allVideos_uz.html'

class OneStudentViewUZ(DetailView):
    model = StudentsModel
    template_name = 'uz/oneStudent_uz.html'

class AllStudentsViewUZ(ListView):
    model = StudentsModel
    template_name = 'uz/allStudents_uz.html'
