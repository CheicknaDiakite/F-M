from django import forms
from .models import Categorie, SousCategorie, OffreRecrutement, OffreDiplome


class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['libelle']


class SousCategorieForm(forms.ModelForm):
    class Meta:
        model = SousCategorie
        fields = ['categorie', 'libelle']


class OffreRecrutementForm(forms.ModelForm):
    class Meta:
        model = OffreRecrutement
        fields = ['categorie', 'libelle']


class OffreDiplomeForm(forms.ModelForm):
    class Meta:
        model = OffreDiplome
        fields = ['diplome', 'offre', 'libelle']
