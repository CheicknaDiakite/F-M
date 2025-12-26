from .models import Categorie


def categories(request):
    """Context processor qui rend toutes les catégories disponibles dans les templates."""
    # Préfetch des sous-catégories pour éviter des requêtes N+1 lors du rendu
    return {"categories": Categorie.objects.prefetch_related('souscategorie_set').all()}
