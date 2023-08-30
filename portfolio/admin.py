from django.contrib import admin
from .models import Portfolio, Projet, Commentaire, Message, Actualite, ImageActualite
# Register your models here.
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'slug', 'categorie', 'image', 'date')

class ProjetAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'slug', 'categorie', 'image', 'lien', 'date')

class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('nom', 'identifiant', 'commentaire', 'image', 'date')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'identifiant', 'message', 'date')

class ActualiteAdmin(admin.ModelAdmin):
    list_display = ('parto', 'titre', 'image', 'description', 'date')

class ImageActualiteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'image', 'post', 'description', 'date')


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Projet, ProjetAdmin)
admin.site.register(Commentaire, CommentaireAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Actualite, ActualiteAdmin)
admin.site.register(ImageActualite, ImageActualiteAdmin)