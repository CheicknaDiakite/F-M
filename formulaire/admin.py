from django.contrib import admin
from .models import Formulaire, SousCategorie, Categorie, Diplome, Epreuve, TypeEpreuve, OffreDiplome, OffreRecrutement


# Register your models here.

@admin.register(Formulaire)
class AdminFormation(admin.ModelAdmin):
    list_display = ["nom", "prenom", "numero"]
    list_filter = ["experience","diplome"]


# Register your models here.
@admin.register(OffreRecrutement)
class AdminOffreRecrutement(admin.ModelAdmin):
    ...


# @admin.register(Formulaire)
# class AdminFormulaire(admin.ModelAdmin):
#     ...


@admin.register(OffreDiplome)
class AdminOffreDiplome(admin.ModelAdmin):
    ...


@admin.register(TypeEpreuve)
class AdminTypeEpreuve(admin.ModelAdmin):
    ...


@admin.register(Epreuve)
class AdminEpreuve(admin.ModelAdmin):
    ...

@admin.register(Diplome)
class AdminDiplome(admin.ModelAdmin):
    ...


@admin.register(Categorie)
class AdminCategorie(admin.ModelAdmin):
    ...


@admin.register(SousCategorie)
class AdminSousCategorie(admin.ModelAdmin):
    ...