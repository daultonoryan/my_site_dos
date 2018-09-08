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
from django.http import Http404
from django.urls import path, re_path, include
from django.shortcuts import render_to_response
from resume.models import Skill, Project, Tool, Work, Eduction, Certification
from rest_framework import routers
import greenthumb.views
from greenthumb.models import Sensors

router = routers.DefaultRouter()
router.register(r'sensors', greenthumb.views.SensorViewSet)
router.register(r"outputs", greenthumb.views.OutputViewSet)



def resume_render(request):
    d = {
        "skills": Skill.objects.all(),
        "projects": Project.objects.all(),
        "tools": Tool.objects.all(),
        "employments": Work.objects.all(),
        "educations": Eduction.objects.all(),
        "certifications": Certification.objects.all()
    }
    return render_to_response("resume2.html", d)


def plant_page_render(request, plant_id):
    valid_urls = Sensors.objects.values_list("unit_id", flat=True)
    if plant_id in valid_urls:
        d = {"item": Sensors.objects.filter(unit_id=plant_id).last()}
        return render_to_response("garden_view.html", d)
    else:
        raise Http404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('daulton_sink_resume/', resume_render),
    path('', resume_render),
    re_path(r'^', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r"sensors/(\S+)", plant_page_render)
]
