from django.urls import path
from . import views

urlpatterns = [
    path("", views.myself, name="myself"),
    path("index/", views.project_index, name="project_index"),
    path("about/", views.about, name="about"),
    path("qualifications/", views.qualifications, name="qualifications"),
    path("skills/", views.skills, name="skills"),
    path("experience/", views.experience, name="experience"),
]