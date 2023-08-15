from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Portfolio(models.Model):
    nom = models.TextField()
    description = models.TextField()
    slug = models.SlugField()
    CATEGORIE_CHOICES = [
        ("ui", "Infographie"),
        ("web", "Design web"),
        ("app", "Developpement web")
        
    ]
    categorie = models.CharField(max_length=20, choices=CATEGORIE_CHOICES, default="ui")
    image = models.ImageField(upload_to='media')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

    class Meta:
        ordering = ['-date']

class Projet(models.Model):
    nom = models.TextField()
    description = models.TextField()
    slug = models.SlugField()
    CATEGORIE_CHOICES = [
        ("web development", "web development"),
    ]
    categorie = models.CharField(max_length=20, choices=CATEGORIE_CHOICES, default="web development")
    image = models.ImageField(upload_to='media')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

    class Meta:
        ordering = ['-date']


class Commentaire(models.Model):
    nom = models.TextField(default="Phantome")
    identifiant = models.TextField()
    commentaire = models.TextField(max_length=100)
    image = models.ImageField(upload_to='media', blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

    class Meta:
        ordering = ['-date']

class Message(models.Model):
    nom = models.TextField(default="Phantome")
    identifiant = models.TextField()
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

    class Meta:
        ordering = ['-date']