import os

from threading import Thread

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from root.mailer import send
from .models import Formulaire, Categorie, OffreRecrutement, SousCategorie


# Create your views here.

def formulaire_index(request):
    categories = Categorie.objects.prefetch_related('souscategorie_set').all()

    # Récupère toutes les offres pour les afficher sur la page d'accueil
    offres = OffreRecrutement.objects.select_related('categorie').all()

    context = {
        "categories": categories,
        "offres": offres,
    }

    # return redirect(reverse("merci"))
    if request.method == "POST":
        form = request.POST

        nom = form.get("nom")
        prenom = form.get("prenom")
        numero = form.get("numero")
        email = form.get("email")
        quartier = form.get("quartier")
        genre = form.get("genre")
        diplome = form.get("diplome")
        experience = form.get("experience")

        cv = request.FILES['cv']
        lettre_motivation = request.FILES['lettre_motivation']
        attestion = request.FILES['attestion']

        name, extension_cv = os.path.splitext(cv.name)
        name, extension_lettre_motivation = os.path.splitext(lettre_motivation.name)
        name, extension_attestion = os.path.splitext(attestion.name)

        if ".pdf" not in extension_cv or ".pdf" not in extension_lettre_motivation or ".pdf" not in extension_attestion:
            messages.warning(request, "Tous les documents doivent être au format PDF")
            return render(request, "formulaire/formulaire_index.html", )

        tmp_cand = Formulaire.objects.all().filter(email=email).first()
        tmp_cand_2 = Formulaire.objects.all().filter(numero=numero).first()

        if tmp_cand or tmp_cand_2:
            messages.warning(request, "Vous avez postuler une fois, Vous ne pouvez pas postuler deux fois")
            return render(request, "formulaire/formulaire_index.html", )

        # TODO verification

        new_formulaire = Formulaire(nom=nom,
                                    prenom=prenom,
                                    numero=numero,
                                    email=email,
                                    genre=genre,
                                    experience=experience,
                                    diplome=diplome,
                                    quartier=quartier,
                                    cv=cv,
                                    lettre_motivation=lettre_motivation,
                                    attestion=attestion)

        new_formulaire.save()

        messages.success(request, "Envoyer !")

        html_message = render_to_string('mail.html',
                                        context={
                                            "sujet": "Candidature Bien reçu",
                                            "message": f"Bonjour <b>{prenom}  {nom}</b> <br><br>"
                                                       f"Nous avons bien reçu votre candidature et nous vous remercions de "
                                                       f"l'intérêt que vous portez à notre entreprise. "
                                                       f"Nous allons étudier votre dossier avec "
                                                       f"attention et nous vous contacterons dans les "
                                                       f"meilleurs délais."
                                                       f"<br><br>",
                                        })

        def task():
            # pour le proprietaire

            send(sujet="Candidature Bien reçu", message="",
                 email_liste=[email],
                 html_message=html_message)

        thread = Thread(target=task)
        thread.start()

        # return redirect(reverse("merci"))

    return render(request, "formulaire/formulaire_index.html", context)


def souscategorie_offres(request, uuid):
    sous = get_object_or_404(SousCategorie, uuid=uuid)
    offres = OffreRecrutement.objects.filter(categorie=sous)

    context = {
        'sous': sous,
        'offres': offres,
    }

    return render(request, 'offres_list.html', context)


def offre_detail(request, uuid):
    offre = get_object_or_404(OffreRecrutement, uuid=uuid)

    # return redirect(reverse("merci"))
    if request.method == "POST":
        form = request.POST

        nom = form.get("nom")
        prenom = form.get("prenom")
        numero = form.get("numero")
        email = form.get("email")
        quartier = form.get("quartier")
        genre = form.get("genre")
        diplome = form.get("diplome")
        experience = form.get("experience")

        cv = request.FILES['cv']
        lettre_motivation = request.FILES['lettre_motivation']
        attestion = request.FILES['attestion']

        name, extension_cv = os.path.splitext(cv.name)
        name, extension_lettre_motivation = os.path.splitext(lettre_motivation.name)
        name, extension_attestion = os.path.splitext(attestion.name)

        if ".pdf" not in extension_cv or ".pdf" not in extension_lettre_motivation or ".pdf" not in extension_attestion:
            messages.warning(request, "Tous les documents doivent être au format PDF")
            return render(request, "formulaire/formulaire_index.html", )

        tmp_cand = Formulaire.objects.all().filter(email=email).first()
        tmp_cand_2 = Formulaire.objects.all().filter(numero=numero).first()

        if tmp_cand or tmp_cand_2:
            messages.warning(request, "Vous avez postuler une fois, Vous ne pouvez pas postuler deux fois")
            return render(request, "formulaire/formulaire_index.html", )

        # TODO verification

        new_formulaire = Formulaire(nom=nom,
                                    prenom=prenom,
                                    numero=numero,
                                    email=email,
                                    genre=genre,
                                    offre=offre,
                                    experience=experience,
                                    diplome=diplome,
                                    quartier=quartier,
                                    cv=cv,
                                    lettre_motivation=lettre_motivation,
                                    attestion=attestion)

        new_formulaire.save()

        messages.success(request, "Envoyer !")

        html_message = render_to_string('mail.html',
                                        context={
                                            "sujet": "Candidature Bien reçu",
                                            "message": f"Bonjour <b>{prenom}  {nom}</b> <br><br>"
                                                       f"Nous avons bien reçu votre candidature et nous vous remercions de "
                                                       f"l'intérêt que vous portez à notre entreprise. "
                                                       f"Nous allons étudier votre dossier avec "
                                                       f"attention et nous vous contacterons dans les "
                                                       f"meilleurs délais."
                                                       f"<br><br>",
                                        })

        def task():
            # pour le proprietaire

            send(sujet="Candidature Bien reçu", message="",
                 email_liste=[email],
                 html_message=html_message)

        thread = Thread(target=task)
        thread.start()

        # return redirect(reverse("merci"))

    #     form = PostuleForm()

    context = {
        'offre': offre,
        # 'form': form,
    }

    return render(request, 'offre_detail.html', context)


def merci(request):
    return render(request, "formulaire/merci.html")


def connexion(request):
    # Si la personne est déjà connectée
    if request.user.is_authenticated:
        # messages.success(request, "Vous êtes déjà connecter")
        return redirect(reverse(administration))

    if request.method == "POST":
        form = request.POST
        username = form.get("username")
        password = form.get("password")
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            messages.success(request, "Vous êtes connecter")

            login(request, user)

            return redirect(reverse(administration))
        else:
            messages.error(request, "Nom utilisateur ou mot de passe incorrect")

    return render(request, "formulaire/connexion.html")


def administration(request, page="tous"):
    if not request.user.is_authenticated:
        # messages.success(request, "Vous êtes déjà connecter")
        return redirect(reverse(connexion))
    all_candidat = Formulaire.objects.all().filter(preselectionner=False).filter(rejeter=False)

    if page:
        if page == "preselectionner":
            all_candidat = Formulaire.objects.all().filter(preselectionner=True)

        if page == "rejeter":
            all_candidat = Formulaire.objects.all().filter(rejeter=True)

    context = {}
    context["genre"] = "tous"
    context["experience"] = "tous"
    context["diplome"] = "tous"

    if request.method == "POST":
        form = request.POST

        liste_select = form.getlist("liste_select")

        if "filter" in form:
            genre = form.get("genre")
            experience = form.get("experience")
            diplome = form.get("diplome")

            context["genre"] = genre
            context["experience"] = experience
            context["diplome"] = diplome

            if diplome != "tous":
                all_candidat = all_candidat.filter(diplome=diplome)

            if experience != "tous":
                all_candidat = all_candidat.filter(experience=experience)

            if genre != "tous":
                all_candidat = all_candidat.filter(genre=genre)

            messages.success(request, f"{len(all_candidat)} candidat(s) trouvé")

        all_selected_candidat = list()
        for id in liste_select:
            tmp_candidat = Formulaire.objects.all().filter(id=id).first()
            if tmp_candidat:
                all_selected_candidat.append(tmp_candidat)

        if "contacter" in form:

            if len(liste_select) == 0:
                messages.success(request, "selectionner des candidats")
            else:
                id_liste = "-".join(liste_select)

                return redirect(reverse('contact_candidat', kwargs={'id_liste': id_liste}))

        if "preselectionner" in form:
            for cand in all_selected_candidat:
                cand.rejeter = False
                cand.preselectionner = True
                cand.save()

        if "entente" in form:
            for cand in all_selected_candidat:
                cand.rejeter = False
                cand.preselectionner = False
                cand.save()

        if "rejeter" in form:
            for cand in all_selected_candidat:
                cand.rejeter = True
                cand.preselectionner = False
                cand.save()
        #
        # if len(all_selected_candidat) > 0 and ("rejeter" in form
        #                                        or "entente" in form
        #                                        or "preselectionner" in form or "contacter" in form):
        #     messages.success(request, f"{len(all_selected_candidat)} candidat(s) Modifier")
        # else:
        #     messages.warning(request, "il faut select des éléments")

    nombre_candidat = len(Formulaire.objects.all())
    nombre_candidat_entente = len(Formulaire.objects.all().filter(preselectionner=False).filter(rejeter=False))
    nombre_preselectionner = len(Formulaire.objects.all().filter(preselectionner=True))
    nombre_rejeter = len(Formulaire.objects.all().filter(rejeter=True))

    context["all_candidat"] = all_candidat
    context["nombre_candidat"] = nombre_candidat
    context["nombre_preselectionner"] = nombre_preselectionner
    context["nombre_rejeter"] = nombre_rejeter
    context["nombre_candidat_entente"] = nombre_candidat_entente
    context["page"] = page
    return render(request, "formulaire/administration.html", context=context)


def contact_candidat(request, id_liste):
    if not request.user.is_authenticated:
        # messages.success(request, "Vous êtes déjà connecter")
        return redirect(reverse(connexion))

    if request.method == "POST":
        form = request.POST
        liste_id = id_liste.split("-")

        sujet = form.get("sujet")
        message = form.get("message")

        html_message = render_to_string('mail.html',
                                        context={
                                            "sujet": sujet,
                                            "message": message,
                                        })

        mail_liste = list()

        for id in liste_id:
            tmp_candidat = Formulaire.objects.all().filter(id=id).first()
            if tmp_candidat:

                mail_liste.append(tmp_candidat)

        def task():
            # pour le proprietaire

            for cand in mail_liste:
                print("test email ..",cand.email)
                send(sujet=sujet, message="",
                     email_liste=[cand.email],
                     html_message=html_message)
                cand.contacter = True
                cand.save()

        thread = Thread(target=task)
        thread.start()

        messages.success(request, f"{len(mail_liste)} emails envoyer")
        return redirect(reverse("administration"))

    context = {}
    nombre_candidat = len(Formulaire.objects.all())
    nombre_preselectionner = len(Formulaire.objects.all().filter(preselectionner=True))
    nombre_rejeter = len(Formulaire.objects.all().filter(rejeter=True))

    # context["all_candidat"] = all_candidat
    context["nombre_candidat"] = nombre_candidat
    context["nombre_preselectionner"] = nombre_preselectionner
    context["nombre_rejeter"] = nombre_rejeter

    return render(request, "formulaire/administration_contacter.html", context=context)


def detaille_candidat(request, id):
    if not request.user.is_authenticated:
        # messages.success(request, "Vous êtes déjà connecter")
        return redirect(reverse(connexion))

    candidat = Formulaire.objects.all().filter(id=id).first()

    if candidat:
        candidat.cv_lien = request.build_absolute_uri(candidat.cv.url)
        candidat.lettre_motivation_lien = request.build_absolute_uri(candidat.lettre_motivation.url)
        candidat.attestion_lien = request.build_absolute_uri(candidat.attestion.url)

        if request.method == "POST":
            form = request.POST

            if "contacter" in form:
                return redirect(reverse('contact_candidat', kwargs={'id_liste': id}))

            if "preselectionner" in form:
                candidat.preselectionner = True
                candidat.rejeter = False
                candidat.save()
                messages.success(request, "Candidat preselectionner")

            if "rejeter" in form:
                candidat.rejeter = True
                candidat.preselectionner = False
                candidat.save()
                messages.success(request, "Candidat rejeter")

            if "atente" in form:
                candidat.rejeter = False
                candidat.preselectionner = False
                candidat.save()
                messages.success(request, "Candidat mise en attente")

    context = {}
    nombre_candidat = len(Formulaire.objects.all())
    nombre_preselectionner = len(Formulaire.objects.all().filter(preselectionner=True))
    nombre_rejeter = len(Formulaire.objects.all().filter(rejeter=True))

    # context["all_candidat"] = all_candidat
    context["nombre_candidat"] = nombre_candidat
    context["nombre_preselectionner"] = nombre_preselectionner
    context["nombre_rejeter"] = nombre_rejeter
    context["candidat"] = candidat

    return render(request, "formulaire/administration_candidat_detail.html", context=context)


def deconnection(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecter")
    return redirect(reverse(connexion))
