from django.urls import path
from . import views
from .views import home, contact, portfolio
from django.views.generic import TemplateView

urlpatterns = [
    path('', home, name="acceuil"),
    path('contact', contact, name="message"),
    path('portfolio', portfolio, name ='portfolio')
    #path('', TemplateView.as_view(template_name='blog/index.html'), name='home'),
]