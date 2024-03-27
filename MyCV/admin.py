from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import *

class BeritaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("title", "description", "image_tag",)
    search_fields = ("title",)
    list_filter = ("title",)

admin.site.register(Berita, BeritaAdmin)

class ReviewAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("name", "email", "review", "image_tag",)
    search_fields = ("name__startswith",)
    list_filter = ("name",)

admin.site.register(Review, ReviewAdmin)
    
    
admin.site.site_header = "Admin Toko Buku"
admin.site.site_title = "Toko Buku"
admin.site.index_title = "Admin Malik"