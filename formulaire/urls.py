from django.urls import path

from .views import formulaire_index, merci, connexion, administration, deconnection, contact_candidat, \
    detaille_candidat, souscategorie_offres, offre_detail

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

]
