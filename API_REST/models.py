from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True,blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=400, null=True)

    def __str__(self):
        if self.name == None:
            return "ERROR-PRODUCT NAME IS NULL" #méthode pour contourner le string non null en base et pouvoir le supprimer
        return self.name
