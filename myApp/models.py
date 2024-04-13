from django.db import models

class CarouselModel(models.Model):
    carousel_text_uz = models.CharField(max_length=200)
    carousel_subtext_uz = models.CharField(max_length=250)
    carousel_photo = models.ImageField(upload_to='carousel/')

    def __str__(self):
        return self.carousel_text_uz
    
class NewsModel(models.Model):
    news_theme_uz = models.CharField(max_length=200)
    news_short_description_uz = models.TextField() 
    news_full_description_uz = models.TextField()
    news_photo = models.ImageField(upload_to='news/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.news_theme_uz
    
class ProjectsCategoryModel(models.Model):
    category_name_uz = models.CharField(max_length=100)
    category_text_uz = models.CharField(max_length=250)
    category_photo = models.ImageField(upload_to='projects_category/')

    def __str__(self):
        return self.category_name_uz
    
class ProjectsModel(models.Model):
    project_name_uz = models.CharField(max_length=100)
    project_subtext_uz = models.CharField(max_length=250)
    project_text_uz = models.TextField()
    project_photo = models.ImageField(upload_to='projects/')
    project_category = models.ForeignKey(ProjectsCategoryModel, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.project_name_uz
    
class ProjectVideosModel(models.Model):
    video_name_uz = models.CharField(max_length=100)
    video_text_uz = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='project_videos/')

    def __str__(self):
        return self.video_name_uz
    
class StudentsModel(models.Model):
    student_fullname_uz = models.CharField(max_length=50)
    student_info_uz = models.CharField(max_length=200)
    student_photo = models.ImageField(upload_to='students/')
    student_link1 = models.CharField(max_length=100)
    student_link2 = models.CharField(max_length=100)
    student_link3 = models.CharField(max_length=100)
    student_link4 = models.CharField(max_length=100)

    def __str__(self):
        return self.student_fullname_uz
    
class PartnersModel(models.Model):
    partner_name = models.CharField(max_length=100)
    partner_link = models.CharField(max_length=200)
    partner_photo = models.ImageField(upload_to='partners/')

    def __str__(self):
        return self.partner_name


