from django import template

register = template.Library()

@register.filter
def fix_media_path(chemin):
    # Convertir le chemin Windows en chemin URL relatif au dossier media
    if not chemin:
        return ''
    # Remplacer les backslashes Windows par des slashes Unix
    chemin = chemin.replace('\\', '/')
    # Retirer le préfixe 'images/' pour servir depuis /media/
    if chemin.startswith('images/'):
        chemin = chemin[len('images/'):]
    return chemin
