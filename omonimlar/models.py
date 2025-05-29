from django.db import models

# Create your models here.

class Omonimlar(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'omonimlar'
        ordering = ['name']

class OmonimTafsiloti(models.Model):
    omonim = models.ForeignKey(Omonimlar, on_delete=models.CASCADE)
    kelib_chiqishi = models.CharField(max_length=100)
    etimologiyasi = models.TextField()
    soz_turkum = models.CharField(max_length=25)
    lugaviy_manosi = models.TextField()
    misol = models.TextField()
    def __str__(self):
        return self.omonim.name
    class Meta:
        db_table = 'omonimlar_tafsiloti'
        ordering = ['omonim']

