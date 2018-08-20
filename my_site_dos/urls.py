"""my_site_dos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.shortcuts import render_to_response
from resume import models
from rest_framework import routers
import greenthumb.views


router = routers.DefaultRouter()
router.register(r'sensors', greenthumb.views.SensorViewSet)



def resume_render(request):
    d = {
        "skills": models.Skill.objects.all(),
        "projects": models.Project.objects.all(),
        "tools": models.Tool.objects.all(),
        "employments": models.Work.objects.all(),
        "educations": models.Eduction.objects.all(),
        "certifications": models.Certification.objects.all()
    }
    return render_to_response("resume2.html", d)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('daulton_sink_resume/', resume_render),
    path('', resume_render),
    re_path(r'^', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
