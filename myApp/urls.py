from django.urls import path
from .views import *

urlpatterns = [
    path('', homePageViewUZ, name="HomePage_UZ"),
    path('allNewsUZ', allNewsViewUZ, name="allNewsUZ"),
    path('newsDetailUZ/<int:pk>/', OneNewsViewUZ.as_view(), name='oneNewsDetailUZ'),
    path('allProjectsView/<str:pk>/', allProjectsViewUZ, name="allProjectsUZ"),
    path('projectsDetailUZ/<int:pk>/', OneProjectViewUZ.as_view(), name="oneProjectDetailUZ"),
    path('allVideosUZ', AllVideosViewUZ.as_view(), name="allVideosUZ"),
    path('studentsDetailUZ/<int:pk>/', OneStudentViewUZ.as_view(), name="oneStudentDetailUZ"),
    path('allStudentsViewUZ', AllStudentsViewUZ.as_view(), name="allStudentsViewUZ"),
]