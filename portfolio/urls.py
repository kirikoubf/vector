from django.urls import path
from . import views
from .views import home, contact, portfolio, actualite, imageactualite, profil_actualite
from django.views.generic import TemplateView

urlpatterns = [
    path('', home, name="acceuil"),
    path('contact', contact, name="message"),
    path('portfolio', portfolio, name ='portfolio'),
    path('actualites', actualite, name ='actualites'),
    path('partenaire', imageactualite, name ='parto'),
    path('actualites/<int:actu_id>/', profil_actualite, name='profil_actualite')

    #path('', TemplateView.as_view(template_name='blog/index.html'), name='home'),
]