from django.db import models
from django.utils.html import mark_safe

# Create your models here.
class Buku(models.Model):

    # fields of the model
    ID_Buku = models.CharField(max_length=5)
    Kategori = models.CharField(max_length = 500)
    Nama_Buku = models.CharField(max_length = 200)
    Harga = models.IntegerField()
    Stok = models.IntegerField()
    Penerbit = models.CharField(max_length=200)
    Image = models.ImageField(upload_to='images', default='')

    # def __str__(self):
    #     return f"{self.ProductID} {self.ProductName} {self.Description} {self.SupplierID} {self.CategoryID} {self.Unit} {self.Price} {self.Image}"

    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.Image.url))
    image_tag.short_description = 'Image'
    
class Penerbit(models.Model):

    # fields of the model
    ID_Penerbit = models.CharField(max_length=5)
    Nama = models.CharField(max_length = 200)
    Alamat = models.CharField(max_length = 200)
    Kota = models.CharField(max_length=200)
    Telepon = models.CharField(max_length=200)
    Image = models.ImageField(upload_to='images', default='')

    # def __str__(self):
    #     return f"{self.ProductID} {self.ProductName} {self.Description} {self.SupplierID} {self.CategoryID} {self.Unit} {self.Price} {self.Image}"

    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.Image.url))
    image_tag.short_description = 'Image'