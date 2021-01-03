from django.db import models

# Create your models here.

class data_mhs(models.Model):
    username = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    nim_tpb = models.IntegerField(primary_key=True,unique=True)
    nim_jurusan = models.IntegerField()
    angkatan = models.IntegerField()
    fakultas = models.CharField(max_length=80)
    jurusan = models.CharField(max_length=80)
    status = models.enums.TextChoices('Mahasiswa','Alumni')

class email_mhs(models.Model):
    nim_tpb = models.ForeignKey(data_mhs,on_delete=models.CASCADE)
    email = models.CharField(max_length=100)

