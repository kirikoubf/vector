from django.shortcuts import render, redirect
from .models import Portfolio, Projet, Message, Commentaire, Actualite
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def home(request):
    if request.method == "GET":
        # Récupérer les objets des modèles pour les afficher dans le template
        portfolios = Portfolio.objects.all()
        projets = Projet.objects.all()
        messages = Message.objects.all()
        commentaires = Commentaire.objects.all()
        

        context = {"portfolios": portfolios, "projets": projets, "messages": messages, "commentaires": commentaires}
        return render(request, "blog/index.html", context=context)

    if request.method == "POST":
        # Récupérer les données du formulaire
        nom = request.POST.get("nom")
        email = request.POST.get("email")
        telephone = request.POST.get("telephone")
        image = request.FILES.get("image")
        commentaire_texte = request.POST.get("commentaire")
        # Créer un nouvel objet Commentaire et l'enregistrer dans la base de données
        nouveau_commentaire = Commentaire(nom=nom, identifiant=telephone, image=image, commentaire=commentaire_texte)
        nouveau_commentaire.save()
        # Rediriger vers l'URL 'acceuil' après avoir enregistré le commentaire
        return redirect('acceuil')

def contact(request):
        if request.method == "GET":
            return render(request, 'blog/contact.html')

        if(request.method == "POST"):
                nom = request.POST.get('nom')
                identifiant = request.POST.get('identifiant')
                message = request.POST.get('message')

                message = Message(nom=nom, identifiant=identifiant, message=message)
                message.save()
                return redirect('acceuil')

def portfolio(request):
    if request.method == "GET":
        portfolios = Portfolio.objects.all()
        context = {"portfolios": portfolios}
        return render(request, 'blog/portfolio.html', context=context)

def actualite(request):
    if request.method == "GET":
        actualites = Actualite.objects.all()
        context = {"actualites": actualites}
        return render(request, 'blog/actualite.html', context=context)