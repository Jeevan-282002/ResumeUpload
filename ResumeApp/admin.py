from django.contrib import admin
from.models import ResumeModel

# Register your models here.

@admin.register(ResumeModel)
class ResumeAdmin(admin.ModelAdmin):
    list_display=['id','fname','lname','email','contact','gender','dob','city','state','language','programming_language','education','prefered_loc','prof_image','project']