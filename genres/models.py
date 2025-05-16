from django.db import models
class coll(models.Model):
    collName = models.CharField(max_length=100)
    collDesc = models.CharField(max_length=500)
    collCover = models.CharField(max_length=1000)

    def __str__(self):
        return self.collName

class piece(models.Model):
    Coll = models.ForeignKey(coll,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    year = models.IntegerField()
    pieceCover = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


# Create your models here.
