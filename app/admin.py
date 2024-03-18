from django.contrib import admin
from app.models import Jobpost, Location, Author, Skills



class JobAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'salary', 'date')
    list_filter = ('date', 'salary')
    search_fields = ('title', 'salary')
    search_help_text = ('search here')
    fieldsets = (
        ('Basic information', {
            'fields':('title', 'description')
        }),

        ('More information', {
            'classes':('collapse',),
            'fields':(('salary'), 'slug')
        }),
    )


# Register your models here.
    
admin.site.register(Jobpost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)