from django.contrib import admin
from django import forms
from .models import *
# from gestschools.models import Eleve,Programme_trans,Bus,Zone,Service,Personnel,Fraispayer,Typefrais,Enseignant_titulaire,Animateur_pedagogique,Ancien_etablissement,Etablissement,Emploi_temps,Absence,Preinscription,Cycle,Affecter_classe,Serie,Periodeeval,Evaluation,Affectation,Discipline_competence,Region,Programme,Groupematiere,Matiere,Trimestre,Sequence,Niveau,Anneescolaire,Registration,Parents,Ville,Arrondissement,Pays,Departementgeo,Region,Enseignant,Classe
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
    get_user_model

)
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import StrictButton
#from bootstrap3_datetime.widgets import DateTimePicker
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import TabHolder, Tab
from captcha.fields import CaptchaField




User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)

class ConnexionForm(forms.Form):
	username=forms.CharField(label="Nom d'utilisateur")
	password=forms.CharField(label="Mot de passe", widget=forms.PasswordInput)



class LockscreenForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        password = self.cleaned_data.get('password')

        if password:
            user = authenticate(password=password)
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
        return super(LockscreenForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    email2 = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "This email has already been registered")
        return super(UserRegisterForm, self).clean(*args, **kwargs)

# Formulaire d'enregistrement d'un enseignant 
class Dateinput(forms.DateInput):
    input_type= 'date'
class EnseignantForm(forms.ModelForm):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Enseignant
        exclude=('compte_utilisateur',)
        widgets={
            'date_naiss':Dateinput(),
            'dataentreefonctionpublique':Dateinput(),
            'datemiseretraite':Dateinput()
        }

class AdminForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for _, value in self.fields.items():
			value.widget.attrs['placeholder'] = value.label
			value.widget.attrs['class'] = 'form-control required'

	class Meta:
		model=Administrateur
		exclude=('compte_utilisateur',)
		# fields='__all__'
		widgets = {
			'date_naiss': Dateinput()
		}
class Dateinput2(forms.DateInput):
    input_type= 'date'
class EtablissementForm(forms.ModelForm):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Etablissement
        fields='__all__'
        widgets={
            'datecreationetab':Dateinput(),
            'datetransformetab':Dateinput()
        }
class Dateinput3(forms.DateInput):
    input_type= 'date'
class Animateur_pedagogiqueForm(forms.ModelForm):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Animateur_pedagogique
        fields='__all__'
        widgets={
            'dateselection':Dateinput()
        }
class Dateinput5(forms.DateInput):
    input_type= 'date'     
class Enseignant_titulaireForm(forms.ModelForm):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Enseignant_titulaire
        fields='__all__'
        widgets={
            'dateaffectation':Dateinput()
        }
class Ancien_etablissementForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model=Ancien_etablissement
        fields='__all__'

class QualificationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model=Qualification
        fields='__all__'
# Enregistrement de l'élève

class Dateinput1(forms.DateInput):
    input_type= 'date'
class EleveForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model=Eleve
        fields='__all__'
        widgets={
            'datenaissel':Dateinput1()
        }

class MatiereForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model=Matiere
        fields='__all__'

class ProgrammeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model=Programme
        fields='__all__'

class GroupematiereForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model=Groupematiere
        fields='__all__' 

class Discipline_competenceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model=Discipline_competence
        fields='__all__' 

class AffectationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model=Affectation
        fields='__all__' 

# Enregistrement des niveaux
class NiveauForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model=Niveau
        fields='__all__'
class Dateinput8(forms.DateInput):
    input_type= 'date'
class AnneescolaireForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model=Anneescolaire
        fields='__all__'
        widgets={
            'datedebut':Dateinput8(),
            'datefin':Dateinput8()
        }

    
class TrimestreForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model=Trimestre
        fields='__all__'  

class SequenceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model=Sequence
        fields='__all__'
        widgets={
            'datedebut':Dateinput8(),
            'datefin':Dateinput8()
        }

class EvaluationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model=Evaluation
        fields='__all__'
        widgets={
            'dateeval':Dateinput8()
        }
class EvaluernoteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model=Evaluernote
        fields='__all__'
      


class PeriodeevalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model=Periodeeval
        fields='__all__'
        widgets={
            'datedebut':Dateinput8(),
            'datefin':Dateinput8()
        }


class PaysForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Pays
        
        fields='__all__'

class RegionForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Region
        fields='__all__'      
class DepartementgeoForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Departementgeo
        fields='__all__'  

class ArrondissementForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Arrondissement
        fields='__all__'   
class VilleForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Ville
        fields='__all__' 

class ParentsForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Parents
        fields='__all__'

class SerieForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Serie
        fields='__all__'

class ClasseForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Classe
        fields='__all__'

class CycleForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Cycle
        fields='__all__'

class Affecter_classeForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Affecter_classe
        fields='__all__'

class PreinscriptionForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Preinscription
        fields='__all__'
class AbsenceForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Absence
        fields='__all__'
class Emploi_tempsForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Emploi_temps
        fields='__all__'
class TypefraisForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Typefrais
        fields='__all__'

class FraispayerForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Fraispayer
        fields='__all__'


class ServiceForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Service
        fields='__all__'

class PersonnelForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Personnel
        exclude=('compte_utilisateur',)
        widgets={
            'date_naiss':Dateinput(),
            'datedelivcni':Dateinput(),
            'dateentreefctpub':Dateinput()
        }

class Programme_transForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Programme_trans
        fields='__all__'
        widgets={
            'date':Dateinput8(),
            
        }
class BusForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Bus
        fields='__all__'
class ZoneForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Zone
        fields='__all__'

class EleveconForm(forms.ModelForm):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Elevecon
        fields='__all__'
        widgets={
            'datenaisselevec':Dateinput(),
        }

class ConcoursForm(forms.ModelForm):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Concours
        fields='__all__'
        widgets={
            'datedebutcon':Dateinput(),
            'datefincon':Dateinput(),
        }

class InscriptionConForm(forms.ModelForm):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= InscriptionCon
        fields='__all__'
        widgets={
            'dateinscription':Dateinput(),
            'dateinscriptionConfirme':Dateinput(),
        }

class EleverecruterForm(forms.ModelForm):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Eleverecruter
        fields='__all__'
        widgets={
            'datederecrute':Dateinput(),
            'dateConfirmerecrute':Dateinput(),
        }
class MatiereconcoursForm(forms.ModelForm):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Matiereconcours
        fields='__all__'

class JoursForm(forms.ModelForm):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Jours
        fields='__all__'

class ProgrammationForm(forms.ModelForm):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Programmation
        fields='__all__'

class CoursLundiForm(forms.ModelForm):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= CoursLundi
        fields='__all__'

class CoursMardiForm(forms.ModelForm):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= CoursMardi
        fields='__all__'

class CoursMercrediForm(forms.ModelForm):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= CoursMercredi
        fields='__all__'
class CoursJeudiForm(forms.ModelForm):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= CoursJeudi
        fields='__all__'
class CoursVendrediForm(forms.ModelForm):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= CoursVendredi
        fields='__all__'
class CoursSamediForm(forms.ModelForm):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= CoursSamedi
        fields='__all__'

class MoyennesequentielForm(forms.ModelForm):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Moyennesequentiel
        fields='__all__'
class CertificatForm(forms.ModelForm):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Certificatsco
        fields='__all__'
class ConseildisciplineForm(forms.ModelForm):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Conseildiscipline
        fields='__all__'
        widgets={
            'dateconseil':Dateinput(),
        }
class DecisionconseilForm(forms.ModelForm):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Decisionconseil
        fields='__all__'
class DecisionfinalconseilForm(forms.ModelForm):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Decisionfinalconseil
        fields='__all__'
class StatutenseignantForm(forms.ModelForm):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Statutenseignant
        fields='__all__'
class Type_contratForm(forms.ModelForm):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label
    class Meta:
        model= Type_contrat
        fields='__all__'
