from django.urls import path

from .views import formulaire_index, merci, connexion, administration, deconnection, contact_candidat, \
    detaille_candidat, souscategorie_offres, offre_detail, ajouter_categorie, ajouter_souscategorie, ajouter_offre_recrutement, ajouter_offre_diplome

urlpatterns = [
    path('', formulaire_index, name="formulaire_index"),
    path('souscategorie/<uuid:uuid>/', souscategorie_offres, name='souscategorie_offres'),
    path('offre/<uuid:uuid>/', offre_detail, name='offre_detail'),
    path('Merci', merci, name="merci"),
    path('connexion', connexion, name="connexion"),
    path('deconnection', deconnection, name="deconnection"),
    path('administration', administration, name="administration"),
    path('administration/<str:page>', administration, name="administration"),
    path('contact_candidat/<str:id_liste>', contact_candidat, name="contact_candidat"),
    path('detaille_candidat/<str:id>', detaille_candidat, name="detaille_candidat"),
    path('gestion/categorie/ajouter/', ajouter_categorie, name='gestion_ajouter_categorie'),
    path('gestion/souscategorie/ajouter/', ajouter_souscategorie, name='gestion_ajouter_souscategorie'),
    path('gestion/offre/ajouter/', ajouter_offre_recrutement, name='gestion_ajouter_offre'),
    path('gestion/offrediplome/ajouter/', ajouter_offre_diplome, name='gestion_ajouter_offrediplome'),

]
