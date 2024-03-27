from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import *

class BukuAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("ID_Buku", "Kategori", "Nama_Buku", "Harga", "Stok", "Penerbit", "image_tag")
    search_fields = ("Nama_Buku__startswith",)
    list_filter = ("ID_Buku",)

admin.site.register(Buku, BukuAdmin)

class PenerbitAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("ID_Penerbit", "Nama", "Alamat", "Kota", "Telepon",)
    search_fields = ("Nama__startswith",)
    list_filter = ("ID_Penerbit",)

admin.site.register(Penerbit, PenerbitAdmin)
    
    
admin.site.site_header = "Admin Toko Buku"
admin.site.site_title = "Toko Buku"
admin.site.index_title = "Admin Malik"
    
