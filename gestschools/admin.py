from django.contrib import admin
from django.contrib.sites.models import Site
#from .models import Moyennesequentiel,Trimestre,Sequence,Fraispayer,Anneescolaire,Matiere,Eleve,Parents,Ville,Arrondissement,Pays,Departementgeo,Region,Enseignant
from .models import *


# Register your models here.
#admin.site.register(Eleve)
admin.site.register(Enseignant_titulaire)

admin.site.register(Parents)
admin.site.register(Evaluernote)
admin.site.register(Ville)
admin.site.register(Arrondissement)
admin.site.register(Departementgeo)
admin.site.register(Compteutilisateur)
#admin.site.register(Region)
#admin.site.register(Pays)
admin.site.register(Enseignant)
admin.site.register(Matiere)
admin.site.register(Groupematiere)
admin.site.register(Programme)
admin.site.register(Sequence)
admin.site.register(Anneescolaire)
admin.site.register(Fraispayer)
admin.site.register(Trimestre)
admin.site.register(Moyennesequentiel)
admin.site.register(Niveau)
admin.site.register(Serie)
admin.site.register(Typefrais)
class EleveAdmin(admin.ModelAdmin):
    model = Eleve
    #inlines = [ProductItemAdmin,]
    search_fields = ('id', 'nom')
    #list_display = ["id", "codeeleve", "matriculeeleve", "civilite", "nom","prenom", "lieunaiss", "datenaiss", "sexe", "nationalite", "emaileleve","teleeleve", "adresseeleve", "handicape", "langueofficielle", "numeroinscription"]
    #list_editable = ["codeeleve", "matriculeeleve", "civilite", "nom","prenom", "lieunaiss", "datenaiss", "sexe", "nationalite", "emaileleve","teleeleve", "adresseeleve", "handicape", "langueofficielle", "numeroinscription"]
admin.site.register(Eleve, EleveAdmin)





#class EleveInline(admin.StackedInline):
   # model = Eleve
    #extra= 1

#class ParentsAdmin(admin.ModelAdmin):

    #inlines = [EleveInline]

class RegionInline(admin.StackedInline):
    model = Region
    extra= 1

class PaysAdmin(admin.ModelAdmin):

    inlines = [RegionInline]

#admin.site.register(Parents, ParentsAdmin)
admin.site.register(Pays, PaysAdmin)





