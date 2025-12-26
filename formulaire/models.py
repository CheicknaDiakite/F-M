from django.db import models
import uuid

class Categorie(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    libelle = models.CharField(max_length=500, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.libelle

    @property
    def sous_categorie(self):
        return self.souscategorie_set.all()


class Diplome(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    libelle = models.CharField(max_length=500, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.libelle


class SousCategorie(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    libelle = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def all_entrer(self):
        return self.entrer_set.all()


class OffreRecrutement(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    categorie = models.ForeignKey(SousCategorie, on_delete=models.CASCADE)

    libelle = models.CharField(max_length=500, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.libelle


class OffreDiplome(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    diplome = models.ForeignKey(Diplome, on_delete=models.CASCADE)
    offre = models.ForeignKey(OffreRecrutement, on_delete=models.CASCADE)

    libelle = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True, null=True)


# Create your models here.
class Formulaire(models.Model):
    # uuid = models.UUIDField(default=uuid.uuid4, editable=False, null=True, blank=True, unique=True)

    offre = models.ForeignKey(OffreRecrutement, on_delete=models.CASCADE, null=True, blank=True)
    diplome_s = models.ForeignKey(Diplome, on_delete=models.CASCADE, null=True, blank=True)

    nom = models.CharField(max_length=255, null=True, blank=True)
    prenom = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    quartier = models.CharField(max_length=255, null=True, blank=True)
    genre = models.CharField(max_length=255, null=True, blank=True)
    numero = models.CharField(max_length=30, null=True, blank=True)

    cv = models.FileField(null=True, blank=True)
    lettre_motivation = models.FileField(null=True, blank=True)
    attestion = models.FileField(null=True, blank=True)

    experience = models.CharField(max_length=255, null=True, blank=True)
    diplome = models.CharField(max_length=255, null=True, blank=True)
    preselectionner = models.BooleanField(default=False, null=True, blank=True)
    rejeter = models.BooleanField(default=False, null=True, blank=True)
    contacter = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"


class TypeEpreuve(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    libelle = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True, null=True)


class Epreuve(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    type = models.ForeignKey(TypeEpreuve, on_delete=models.CASCADE)
    diplome = models.ForeignKey(Diplome, on_delete=models.CASCADE)

    statut = models.CharField(max_length=500, null=False, blank=False)
    note = models.IntegerField(default=0)

    date_e = models.DateTimeField(auto_now_add=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
