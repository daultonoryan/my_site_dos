from django.db import models

class Skill(models.Model):
    skill_name = models.CharField(max_length=40, default="STRING")

    def __str__(self):
        return self.skill_name


class Tool(models.Model):
    tool_name = models.CharField(max_length=40, default="STRING")

    def __str__(self):
        return self.tool_name


class Project(models.Model):
    project_name = models.CharField(max_length=40, default="STRING")
    project_path = models.CharField(max_length=40, default="FILE_PATH")
    project_url = models.CharField(max_length=100, default="SITE_URL")

    def __str__(self):
        return self.project_name


class Eduction(models.Model):
    education_name = models.CharField(max_length=40, default="STRING")
    education_institution = models.CharField(max_length=40, default="STRING")
    education_dates = models.CharField(max_length=40, default="STRING")
    education_synopsis1 = models.CharField(max_length=200, default="", blank=True)
    education_synopsis2 = models.CharField(max_length=200, default="", blank=True)
    education_synopsis3 = models.CharField(max_length=200, default="", blank=True)
    education_synopsis4 = models.CharField(max_length=200, default="", blank=True)
    education_synopsis5 = models.CharField(max_length=200, default="", blank=True)

    def __str__(self):
        return self.education_name


class Work(models.Model):
    work_name = models.CharField(max_length=40, default="STRING")
    work_institution = models.CharField(max_length=40, default="STRING")
    work_dates = models.CharField(max_length=40, default="STRING")
    work_synopsis1 = models.CharField(max_length=200, default="", blank=True)
    work_synopsis2 = models.CharField(max_length=200, default="", blank=True)
    work_synopsis3 = models.CharField(max_length=200, default="", blank=True)
    work_synopsis4 = models.CharField(max_length=200, default="", blank=True)
    work_synopsis5 = models.CharField(max_length=200, default="", blank=True)

    def __str__(self):
        return self.work_name

class Certification(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=400, blank=True)
    url = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name




