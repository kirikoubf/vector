from django.contrib import admin
from .models import Portfolio, Projet, Commentaire, Message
# Register your models here.
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'slug', 'categorie', 'image', 'date')

class ProjetAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'slug', 'categorie', 'image', 'date')

class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('nom', 'identifiant', 'commentaire', 'image', 'date')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'identifiant', 'message', 'date')


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Projet, ProjetAdmin)
admin.site.register(Commentaire, CommentaireAdmin)
admin.site.register(Message, MessageAdmin)