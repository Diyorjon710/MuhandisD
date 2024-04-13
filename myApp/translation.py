from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(CarouselModel)
class CaruselTranslationOptions(TranslationOptions):
    fields = ('carousel_text_uz','carousel_subtext_uz')

@register(NewsModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ('news_theme_uz','news_short_description_uz','news_full_description_uz')

@register(ProjectsCategoryModel)
class ProjectCategoryTranslationOptions(TranslationOptions):
    fields = ('category_name_uz','category_text_uz')

@register(ProjectsModel)
class ProjectsTranslationOptions(TranslationOptions):
    fields = ('project_name_uz','project_subtext_uz','project_text_uz')

@register(ProjectVideosModel)
class ProjectVideosTranslationOptions(TranslationOptions):
    fields = ('video_name_uz','video_text_uz')

@register(StudentsModel)
class StudenttranslationOptions(TranslationOptions):
    fields = ('student_fullname_uz','student_info_uz')