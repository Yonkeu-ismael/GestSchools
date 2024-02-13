#-*- coding: utf-8 -*-
from django.core.mail import send_mail
from django.contrib.auth.models import Group,Permission
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .utils import render_to_pdf #created in step 4
from django.template.loader import get_template
from django.template import Context
from django.views.decorators.csrf import csrf_protect 
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView,View,TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg,Max, Min, Sum

from django.http import HttpResponse
from . import forms
from .models import *
from .forms import EleveForm,NiveauForm,DecisionconseilForm,Type_contratForm,DecisionfinalconseilForm,StatutenseignantForm,EtablissementForm,CertificatForm,QualificationForm, EleverecruterForm, MoyennesequentielForm,AdminForm,EvaluernoteForm,MatiereconcoursForm,InscriptionConForm,EleveconForm,ConcoursForm,PersonnelForm,CycleForm,Enseignant_titulaireForm,Emploi_tempsForm,AbsenceForm,PreinscriptionForm,Affecter_classeForm,PeriodeevalForm,AffectationForm,GroupematiereForm,ProgrammeForm,MatiereForm,EnseignantForm,UserLoginForm,LockscreenForm,UserRegisterForm,SequenceForm,TrimestreForm,EvaluationForm
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from django.urls import reverse_lazy
from django.views import generic
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestschools:menu')
    else:
        form = UserCreationForm()
    return render(request, 'gestschools/signup.html', {
        'form': form
    })

def login_view(request): 
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect(menu)

    context = {
        'form': form,
    }
    return render(request, "gestschools/login.html", context)

def admin(request):
    form = forms.AdminForm
    
    if request.method=='POST':
        form = forms.AdminForm(request.POST)
        if form.is_valid():
            mod=Compteutilisateur
            gp=Group.objects.get(name="administration")
            administration=form.save(commit=False)
            nom=form.cleaned_data['nom']
            prenom=form.cleaned_data['prenom']
            email=form.cleaned_data['email']
            username=(nom[0:5]+prenom[0:3]).lower()
            mdp=mod.objects.make_random_password()
            user=mod.objects.create_user(username=username, email=email, password=mdp, first_name=nom, last_name=prenom)
            administration.compte_utilisateur=user
            user.groups.set([gp,])
            permis=Permission.objects.all().filter(group=gp.id)
            for perm in permis:
                user.user_permissions.add(perm)
            administration.save()
            mail(request, emailto=email , nom=nom, prenom=prenom, username=username, mdp=mdp)

            return redirect('gestschools:liste_admin') 
        else:
            return render(request, 'gestschools/admin.html', {'form': form})
    else:
        return render(request, 'gestschools/admin.html', {'form': form})
        
class liste_admin(generic.ListView):
    model = Administrateur
    context_object_name = 'administrateurs'
    template_name = 'liste_admin.html'
def listeadmin(request):
    administrateurs=Administrateur.objects.order_by('nom')
    return render(request, 'liste_admin.html', {'administrateurs': administrateurs})

class AdminUpdateView(UpdateView):
    model = Administrateur
    template_name = 'gestschools/update_admin.html'
    form_class = AdminForm
    success_url = reverse_lazy('gestschools:liste_admin')

class AdminDeleteView(BSModalDeleteView):
    model = Administrateur
    template_name = 'gestschools/delete_admin.html'
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_admin')

class liste_affecterclasse(generic.ListView):
    model = Affecter_classe
    context_object_name = 'affectes'
    template_name = 'liste_affecterclasse.html'
def listeaffecterclasse(request):
    affectes=Affecter_classe.objects.all().order_by('eleve__nom')
    return render(request, 'liste_affecterclasse.html', {'affectes': affectes})

class AffecterUpdateView(UpdateView):
    model = Affecter_classe
    template_name = 'gestschools/update_affecter_classe.html'
    form_class = Affecter_classeForm
    success_url = reverse_lazy('gestschools:liste_affecterclasse')

class AffecterDeleteView(BSModalDeleteView):
    model = Affecter_classe
    template_name = 'gestschools/delete_affecter_classe.html'
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_affecterclasse')


def mail(request, emailto, nom, prenom, username, mdp):
    subject_template_name ='Enregistrement au système GESTSCHOOLS éffectué avec succès'
    template_name =get_template('gestschools/valide.html').render(
        context=
            {'nom':nom, 'prenom':prenom, 'mdp':mdp, 'username':username}
    )
    send_mail(subject=subject_template_name, message=template_name, from_email=settings.EMAIL_HOST_USER, recipient_list=[emailto], )
# class moyennesequentiel(View):
#     def get(self):
#         a = Evaluernote.objects.all()



class GeneratePDF(View):
   
    context_object_name = 'services'
    template_name = 'invoice.html'
    def get(self, request, *args, **kwargs):
        template = get_template('gestschools/invoice.html')
        context = {
            
            "libelleetablng1":"Lycée de Bayangam",
            "bp": "27 TONGA", "tel": "670 72 96 71",
            "email": "lyceebilinguetga@yahoo.fr",
            "libelleetablng2":"G.H.S Bayangam",
            "classe":"6e M1",
            "sequence":"1",
            "anneescolaire":"2019/2020",
            "site":"www.lybay.cm"

            
        }
        html= template.render(context)
        pdf = render_to_pdf('gestschools/invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
class ServicePDF(View):
   
  
    template_name = 'servicePDF.html'
    def get(self, request, *args, **kwargs):
        template = get_template('gestschools/servicePDF.html')
        services=Service.objects.all()
        e=Etablissement.objects.all()

        context = {
            
            "services":services,
            "e":e,
        }
        html= template.render(context)
        pdf = render_to_pdf('gestschools/servicePDF.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Services.pdf"
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")     
class EnseignantPDF(View):
   
  
    template_name = 'enseignantPDF.html'
    def get(self, request, *args, **kwargs):
        template = get_template('gestschools/enseignantPDF.html')
        enseignants=Enseignant.objects.all().order_by('nom')
        e=Etablissement.objects.all()

        context = {
            
            "enseignants":enseignants,
            "e":e,
        }
        html= template.render(context)
        pdf = render_to_pdf('gestschools/enseignantPDF.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Liste des enseignants.pdf"
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")   
class AfectationPDF(View):
   
  
    template_name = 'afectationPDF.html'
    def get(self, request, *args, **kwargs):
        template = get_template('gestschools/afectationPDF.html')
        affectations=Affectation.objects.all().order_by('enseignant__nom')
        e=Etablissement.objects.all()

        context = {
            
            "affectations":affectations,
            "e":e,
        }
        html= template.render(context)
        pdf = render_to_pdf('gestschools/afectationPDF.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Liste des affectations.pdf"
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found") 

class ElevePDF(View):
   
  
    template_name = 'elevePDF.html'
    def get(self, request, *args, **kwargs):
        template = get_template('gestschools/elevePDF.html')
        eleves=Eleve.objects.all().order_by('nom')
        e=Etablissement.objects.all()

        context = {
            
            "eleves":eleves,
            "e":e,
        }
        html= template.render(context)
        pdf = render_to_pdf('gestschools/elevePDF.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Liste des élève.pdf"
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")   
class PersonnelPDF(View):
   
  
    template_name = 'personnelPDF.html'
    def get(self, request, *args, **kwargs):
        template = get_template('gestschools/personnelPDF.html')
        personnels=Personnel.objects.all().order_by('nom')
        e=Etablissement.objects.all()

        context = {
            
            "personnels":personnels,
            "e":e,
        }
        html= template.render(context)
        pdf = render_to_pdf('gestschools/personnelPDF.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Liste du personnel.pdf"
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")   
class ProgrammePDF(View):
   
  
    template_name = 'programmePDF.html'
    def get(self, request, *args, **kwargs):
        template = get_template('gestschools/programmePDF.html')
        programmes=Programme_trans.objects.all().order_by('date')
        e=Etablissement.objects.all()

        context = {
            
            "programmes":programmes,
            "e":e,
        }
        html= template.render(context)
        pdf = render_to_pdf('gestschools/programmePDF.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Programme de transport.pdf"
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")   

class EmploiPDF(View):
   
  
    template_name = 'emploiPDF.html'
    def get(self, request, *args, **kwargs):
        template = get_template('gestschools/emploiPDF.html')
        emplois=Emploi_temps.objects.all().order_by('plage_horaire')
        e=Etablissement.objects.all()

        context = {
            
            "emplois":emplois,
            "e":e,
        }
        html= template.render(context)
        pdf = render_to_pdf('gestschools/emploiPDF.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Emploi de temps.pdf"
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")   

class AffecterclassePDF(View):
   
  
    template_name = 'affecterclassePDF.html'
    def get(self, request, *args, **kwargs):
        template = get_template('gestschools/affecterclassePDF.html')
        affectes=Affecter_classe.objects.all().order_by('eleve__nom')
        e=Etablissement.objects.all()

        context = {
            
            "affectes":affectes,
            "e":e,
        }
        html= template.render(context)
        pdf = render_to_pdf('gestschools/affecterclassePDF.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Liste_des_élèves.pdf"
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")   
# Create your views here.

class liste_eleves(generic.ListView):
    model = Eleve
    context_object_name = 'eleves'
    template_name = 'liste_eleves.html'

def listeeleves(request):
    eleves=Eleve.objects.all().order_by('nom')
    return render(request, 'liste_eleves.html', {'eleves': eleves})


class EleveUpdateView(UpdateView):
    model = Eleve
    template_name = 'gestschools/update_eleve.html'
    form_class = EleveForm
    success_url = reverse_lazy('gestschools:liste_eleves')

class EleveDeleteView(BSModalDeleteView):
    model = Eleve
    template_name = 'gestschools/delete_eleve.html'
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_eleves')

class liste_programme(generic.ListView):
    model = Programme_trans
    context_object_name = 'programmes'
    template_name = 'liste_programme.html'
class ProgrammeDeleteView(BSModalDeleteView):
    model = Programme_trans
    template_name = 'gestschools/delete_programme.html'
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_programme')

class liste_personnel(generic.ListView):
    model = Personnel
    context_object_name = 'personnels'
    template_name = 'liste_personnel.html'

class PersonnelUpdateView(UpdateView):
    model = Personnel
    template_name = 'gestschools/update_personnel.html'
    form_class = PersonnelForm
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_personnel')

class PersonnelDeleteView(BSModalDeleteView):
    model = Personnel
    template_name = 'gestschools/delete_personnel.html'
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_personnel')

class liste_service(generic.ListView):
    model = Service
    context_object_name = 'services'
    template_name = 'liste_service.html'
class liste_invoice(generic.ListView):
    model = Service
    context_object_name = 'services'
    template_name = 'invoice.html'

class ServiceDeleteView(BSModalDeleteView):
    model = Service
    template_name = 'gestschools/delete_service.html'
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_service')

class liste_titulaires(generic.ListView):
    model = Enseignant_titulaire
    context_object_name = 'titulaires'
    template_name = 'liste_titulaires.html'
def listetitulaires(request):
    titulaires=Enseignant_titulaire.objects.order_by('enseignant__nom')
    return render(request, 'liste_titulaires.html', {'titulaires': titulaires})

class TitulaireUpdateView(UpdateView):
    model = Enseignant_titulaire
    template_name = 'gestschools/update_titulaire.html'
    form_class = Enseignant_titulaireForm
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_titulaires')

class TitulaireDeleteView(BSModalDeleteView):
    model = Enseignant_titulaire
    template_name = 'gestschools/delete_titulaire.html'
    success_message = 'Suppression effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_titulaires')

class liste_enseignants(generic.ListView):
    model = Enseignant
    context_object_name = 'enseignants'
    template_name = 'liste_enseignants.html'
def listeenseignants(request):
    enseignants=Enseignant.objects.all().order_by('nom')
    return render(request, 'liste_enseignants.html', {'enseignants': enseignants})

class EnseignantUpdateView(UpdateView):
    model = Enseignant
    template_name = 'gestschools/update_enseignant.html'
    form_class = EnseignantForm
    success_message = 'Success: Enseignant was updated.'
    success_url = reverse_lazy('gestschools:liste_enseignants')

class EnseignantDeleteView(BSModalDeleteView):
    model = Enseignant
    template_name = 'gestschools/delete_enseignant.html'
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_enseignants')

class liste_preinscriptions(generic.ListView):
    model = Preinscription
    context_object_name = 'preinscriptions'
    template_name = 'liste_preinscriptions.html'

class PreinscriptionUpdateView(BSModalUpdateView):
    model = Preinscription
    template_name = 'gestschools/update_preinscription.html'
    form_class = PreinscriptionForm
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_preinscriptions')

class PreinscriptionDeleteView(BSModalDeleteView):
    model = Preinscription
    template_name = 'gestschools/delete_preinscription.html'
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_preinscriptions')

class liste_evaluations(generic.ListView):
    model = Evaluation
    context_object_name = 'evaluations'
    template_name = 'liste_evaluations.html'

class EvaluationUpdateView(BSModalUpdateView):
    model = Evaluation
    template_name = 'gestschools/update_evaluation.html'
    form_class = EvaluationForm
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_evaluations')

class EvaluationDeleteView(BSModalDeleteView):
    model = Evaluation
    template_name = 'gestschools/delete_evaluation.html'
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_evaluations')



class liste_evaluernote(generic.ListView):
    model = Evaluernote
    context_object_name = 'evaluernotes'
    template_name = 'liste_evaluernote.html'

class EvaluernoteUpdateView(BSModalUpdateView):
    model = Evaluernote
    template_name = 'gestschools/update_evaluernote.html'
    form_class = EvaluernoteForm
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_evaluernote')

class EvaluernoteDeleteView(BSModalDeleteView):
    model = Evaluernote
    template_name = 'gestschools/delete_evaluernote.html'
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_evaluernote')

# class liste_programmation(generic.ListView):
#     model = Programmation
#     context_object_name = 'programmations'
#     template_name = 'liste_programmation.html'


class liste_emploi_temps(generic.ListView):
	model = Emploi_temps
	context_object_name = 'emplois'
	template_name = 'liste_emploi_temps.html'

class Emploi_tempsUpdateView(BSModalUpdateView):
    model = Emploi_temps
    template_name = 'gestschools/update_emploi_temps.html'
    form_class = Emploi_tempsForm
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_emploi_temps')

class Emploi_tempsDeleteView(BSModalDeleteView):
    model = Emploi_temps
    template_name = 'gestschools/delete_emploi_temps.html'
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_emploi_temps')


class liste_absences(generic.ListView):
    model = Absence
    context_object_name = 'absences'
    template_name = 'liste_absences.html'
def listeabsences(request):
    absences=Absence.objects.all().order_by('-nonjustifier')
    return render(request, 'liste_absences.html', {'absences': absences})
class AbsencePDF(View):
   
  
    template_name = 'absencePDF.html'
    def get(self, request, *args, **kwargs):
        template = get_template('gestschools/absencePDF.html')
        absences=Absence.objects.all().order_by('-nonjustifier')
        e=Etablissement.objects.all()

        context = {
            
            "absences":absences,
            "e":e,
        }
        html= template.render(context)
        pdf = render_to_pdf('gestschools/absencePDF.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Statistique des absences.pdf"
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found") 

class AbsenceUpdateView(BSModalUpdateView):
    model = Absence
    template_name = 'gestschools/update_absence.html'
    form_class = AbsenceForm
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_absences')

class AbsenceDeleteView(BSModalDeleteView):
    model = Absence
    template_name = 'gestschools/delete_absence.html'
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_absences')


class liste_disciplines(generic.ListView):
    model = Discipline_competence
    context_object_name = 'discipline_competences'
    template_name = 'liste_disciplines.html'

class Discipline_competenceUpdateView(BSModalUpdateView):
    model = Discipline_competence
    template_name = 'gestschools/update_discipline.html'
    form_class = EnseignantForm
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_disciplines')

class Discipline_competenceDeleteView(BSModalDeleteView):
    model = Discipline_competence
    template_name = 'gestschools/delete_discipline.html'
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_disciplines')



class liste_matiere(generic.ListView):
    model = Matiere
    context_object_name = 'matieres'
    template_name = 'liste_matiere.html'

class MatiereUpdateView(BSModalUpdateView):
    model = Matiere
    template_name = 'gestschools/update_matiere.html'
    form_class = MatiereForm
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_matiere')

class MatiereDeleteView(BSModalDeleteView):
    model = Matiere
    template_name = 'gestschools/delete_matiere.html'
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_matiere')


class liste_affectations(generic.ListView):
    model = Affectation
    context_object_name = 'affectations'
    template_name = 'liste_affectations.html'
def listeaffectations(request):
    affectations=Affectation.objects.order_by('enseignant__nom')
    return render(request, 'liste_affectations.html', {'affectations': affectations})

class AffectationUpdateView(BSModalUpdateView):
    model = Affectation
    template_name = 'gestschools/update_affectation.html'
    form_class = AffectationForm
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_affectations')

class AffectationDeleteView(BSModalDeleteView):
    model = Affectation
    template_name = 'gestschools/delete_affectation.html'
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_affectations')

class liste_classes(generic.ListView):
    model = Classe
    context_object_name = 'classes'
    template_name = 'liste_classes.html'

class ClasseDeleteView(BSModalDeleteView):
    model = Classe
    template_name = 'gestschools/delete_classe.html'
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_classes')



def user_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "gestschools/view_user.html", context)

def lockscreen(request):
    next = request.GET.get('next')
    form = LockscreenForm(request.POST or None)
    if form.is_valid():
        password = form.cleaned_data.get('password')
        user = authenticate(password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "gestschools/lockscreen.html", context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "gestschools/signup.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')




def index(request):
	
	return render(request,'gestschools/index.html')

@login_required
def menu(request):
    return render(request, "gestschools/menu.html", {})

def eleve(request):
    form = forms.EleveForm
    return render(request, 'gestschools/eleve.html', {'form': form})

def menueleve(request):
    form = forms.EleveForm
    if request.method=='POST':
        form = forms.EleveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestschools:affecter_classe')
        else:
            return render(request, 'gestschools/menueleve.html', {'form': form})
    else:
        return render(request, 'gestschools/menueleve.html', {'form': form})

def absence(request):
    form = forms.AbsenceForm
    
    if request.method=='POST':
        form = forms.AbsenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestschools:liste_absences')
        else:
            return render(request, 'gestschools/absence.html', {'form': form})
    else:
        return render(request, 'gestschools/absence.html', {'form': form})
    

def enseignant(request):
    form = forms.EnseignantForm
    
    if request.method=='POST':
        form = forms.EnseignantForm(request.POST)
        if form.is_valid():
            mod=Compteutilisateur
            gp=Group.objects.get(name="enseignant")
            enseignant=form.save(commit=False)
            nom=form.cleaned_data['nom']
            prenom=form.cleaned_data['prenom']
            email=form.cleaned_data['email']
            username=(nom[0:5]+prenom[0:3]).lower()
            mdp=mod.objects.make_random_password()
            user=mod.objects.create_user(username=username, email=email, password=mdp, first_name=nom, last_name=prenom)
            enseignant.compte_utilisateur=user
            user.groups.set([gp,])
            permis=Permission.objects.all().filter(group=gp.id)
            for perm in permis:
                user.user_permissions.add(perm)
            enseignant.save()
            mail(request, emailto=email , nom=nom, prenom=prenom, username=username, mdp=mdp)

            return redirect('gestschools:affectation') 
        else:
            return render(request, 'gestschools/enseignant.html', {'form': form})
    else:
        return render(request, 'gestschools/enseignant.html', {'form': form})


def ancienetablissement(request):
    form = forms.Ancien_etablissementForm
    
    if request.method=='POST':
        form = forms.Ancien_etablissementForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('gestschools:ancienetablissement')

        else:
            return render(request, 'gestschools/ancienetablissement.html', {'form': form})
    else:
        return render(request, 'gestschools/ancienetablissement.html', {'form': form})

def animateur_pedagogique(request):
    form = forms.Animateur_pedagogiqueForm
    
    if request.method=='POST':
        form = forms.Animateur_pedagogiqueForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('gestschools:animateurpedagogique')
        else:
            return render(request, 'gestschools/animateurpedagogique.html', {'form': form})
    else:
        return render(request, 'gestschools/animateurpedagogique.html', {'form': form})

def enseignant_titulaire(request):
    form = forms.Enseignant_titulaireForm
    
    if request.method=='POST':
        form = forms.Enseignant_titulaireForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('gestschools:liste_titulaires')
        else:
            return render(request, 'gestschools/enseignant_titulaire.html', {'form': form})
    else:
        return render(request, 'gestschools/enseignant_titulaire.html', {'form': form})

def pays(request):
    form = forms.PaysForm
    if request.method=='POST':
        form = forms.PaysForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestschools:pays')
        else:
            return render(request, 'gestschools/pays.html', {'form': form})
    else:
        return render(request, 'gestschools/pays.html', {'form': form})

def region(request):
    form = forms.RegionForm
    if request.method=='POST':
        form = forms.RegionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestschools:region')
        else:
            return render(request, 'gestschools/region.html', {'form': form})
    else:
        return render(request, 'gestschools/region.html', {'form': form})

def departement(request):
    form = forms.DepartementgeoForm
    if request.method=='POST':
        form = forms.DepartementgeoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestschools:departement')
        else:
            return render(request, 'gestschools/departement.html', {'form': form})
    else:
        return render(request, 'gestschools/departement.html', {'form': form})

def arrondissement(request):
    form = forms.ArrondissementForm
    if request.method=='POST':
        form = forms.ArrondissementForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('gestschools:arrondissement')
        else:
            return render(request, 'gestschools/arrondissement.html', {'form': form})
    else:
        return render(request, 'gestschools/arrondissement.html', {'form': form})

def ville(request):
    form = forms.VilleForm
    if request.method=='POST':
        form = forms.VilleForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('gestschools:ville')
        else:
            return render(request, 'gestschools/ville.html', {'form': form})
    else:
        return render(request, 'gestschools/ville.html', {'form': form})

def matiere(request):
    form = forms.MatiereForm
    if request.method=='POST':
        form = forms.MatiereForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return redirect('gestschools:liste_matiere')
        else:
            return render(request, 'gestschools/matiere.html', {'form': form})
    else:
        return render(request, 'gestschools/matiere.html', {'form': form})


def evaluation(request):
    form = forms.EvaluationForm
    
    if request.method=='POST':
        form = forms.EvaluationForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('gestschools:liste_evaluations')
        else:
            return render(request, 'gestschools/evaluation.html', {'form': form})
    else:
        return render(request, 'gestschools/evaluation.html', {'form': form})

def evaluernote(request):
    form = forms.EvaluernoteForm
    
    if request.method=='POST':
        form = forms.EvaluernoteForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('gestschools:evaluernote')
        else:
            return render(request, 'gestschools/evaluernote.html', {'form': form})
    else:
        return render(request, 'gestschools/evaluernote.html', {'form': form})

def periodeeval(request):
    form = forms.PeriodeevalForm
    if request.method=='POST':
        form = forms.PeriodeevalForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('gestschools:periodeeval')
        else:
            return render(request, 'gestschools/periodeeval.html', {'form': form})
    else:
        return render(request, 'gestschools/periodeeval.html', {'form': form})

def programme(request):
    form = forms.ProgrammeForm
    if request.method=='POST':
        form = forms.ProgrammeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestschools:programme')
        else:
            return render(request, 'gestschools/programme.html', {'form': form})
    else:
        return render(request, 'gestschools/programme.html', {'form': form})


def groupematiere(request):
    form = forms.GroupematiereForm
    if request.method=='POST':
        form = forms.GroupematiereForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('gestschools:groupematiere')
        else:
            return render(request, 'gestschools/groupematiere.html')
    else:
        return render(request, 'gestschools/groupematiere.html', {'form': form})

def discipline_competence(request):
    form = forms.Discipline_competenceForm
    
    if request.method=='POST':
        form = forms.Discipline_competenceForm(request.POST or None)
        if form.is_valid():
            form.save(commit=True)
            return redirect('gestschools:liste_disciplines')
        else:
            return render(request, 'gestschools/discipline_competence.html', {'form': form})
    else:
        return render(request, 'gestschools/discipline_competence.html', {'form': form})

def affectation(request):
    form = forms.AffectationForm
    if request.method=='POST':
        form = forms.AffectationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('gestschools:liste_affectations')
        else:
            return render(request, 'gestschools/affectation.html', {'form': form})
    else:
        return render(request, 'gestschools/affectation.html', {'form': form})

def classe(request):
    form = forms.ClasseForm
    if request.method=='POST':
        form = forms.ClasseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestschools:liste_classes')
        else:
            return render(request, 'gestschools/classe.html', {'form': form})
    else:
        return render(request, 'gestschools/classe.html', {'form': form})


def cycle(request):
    form = forms.CycleForm
    if request.method=='POST':
        form = forms.CycleForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('gestschools:cycle')
        else:
            return render(request, 'gestschools/cycle.html', {'form': form})
    else:
        return render(request, 'gestschools/cycle.html', {'form': form})


def serie(request):
    form = forms.SerieForm
    if request.method=='POST':
        form = forms.SerieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('gestschools:serie')
        else:
            return render(request, 'gestschools/serie.html', {'form': form})
    else:
        
        return render(request, 'gestschools/serie.html', {'form': form})

def parents(request):
    form = forms.ParentsForm
    if request.method=='POST':
        form = forms.ParentsForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('gestschools:parents')
        else:
            return render(request, 'gestschools/parents.html', {'form': form})
    else:
        
        return render(request, 'gestschools/parents.html', {'form': form})

def affecter_classe(request):
    form = forms.Affecter_classeForm
    if request.method=='POST':
        form = forms.Affecter_classeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestschools:liste_affecterclasse')
        else:
            return render(request, 'gestschools/affecter_classe.html', {'form': form})
    else:
        
        return render(request, 'gestschools/affecter_classe.html', {'form': form})


def preinscription(request):
    form = forms.PreinscriptionForm
    
    if request.method=='POST':
        form = forms.PreinscriptionForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('gestschools:liste_preinscriptions')
        else:
            return render(request, 'gestschools/preinscription.html', {'form': form})
    else:
        return render(request, 'gestschools/preinscription.html', {'form': form})

def anneescolaire(request):
    form = forms.AnneescolaireForm
    if request.method=='POST':
        form = forms.AnneescolaireForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('gestschools:anneescolaire')
        else:
            return render(request, 'gestschools/anneescolaire.html', {'form': form})
    else:
        return render(request, 'gestschools/anneescolaire.html', {'form': form})

def trimestre(request):
    form = forms.TrimestreForm
    if request.method=='POST':
        form = forms.TrimestreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestschools:trimestre')
        else:
            return render(request, 'gestschools/trimestre.html', {'form': form})
    else:
        return render(request, 'gestschools/trimestre.html', {'form': form})

def sequence(request):
    form = forms.SequenceForm    
    if request.method=='POST':
        form = forms.SequenceForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('gestschools:sequence')
        else:
            return render(request, 'gestschools/sequence.html')
    else:

        return render(request, 'gestschools/sequence.html', {'form': form})



def moyennesequentiel(request):
    form = forms.MoyennesequentielForm    
    if request.method=='POST':
        form = forms.MoyennesequentielForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('gestschools:moyennesequentiel')
        else:
            return render(request, 'gestschools/moyennesequentiel.html')
    else:

        return render(request, 'gestschools/moyennesequentiel.html', {'form': form})

def typefrais(request):
    form = forms.TypefraisForm
    if request.method=='POST':
        form = forms.TypefraisForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('gestschools:typefrais')
        else:
            return render(request, 'gestschools/typefrais.html', {'form': form})
    else:
        return render(request, 'gestschools/typefrais.html', {'form': form})

def fraispayer(request):
    form = forms.FraispayerForm
    if request.method=='POST':
        form = forms.FraispayerForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('gestschools:fraispayer')
        else:
            return render(request, 'gestschools/fraispayer.html', {'form': form})
    else:
        return render(request, 'gestschools/fraispayer.html', {'form': form})

def service(request):
    form = forms.ServiceForm
    if request.method=='POST':
        form = forms.ServiceForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('gestschools:liste_service')
        else:
            return render(request, 'gestschools/service.html', {'form': form})
    else:
        return render(request, 'gestschools/service.html', {'form': form})

def personnel(request):
    form = forms.PersonnelForm
    
    if request.method=='POST':
        form = forms.PersonnelForm(request.POST)
        if form.is_valid():
            mod=Compteutilisateur
            gp=Group.objects.get(name="personnel")
            personnel=form.save(commit=False)

            personnel.nom= nom = form.cleaned_data['nom'].upper()
            personnel.prenom = prenom = form.cleaned_data['prenom'].title()
            email=form.cleaned_data['email']
            username=(nom[0:5]+prenom[0:3]).lower()
            mdp=mod.objects.make_random_password()
            user=mod.objects.create_user(username=username, email=email, password=mdp, first_name=nom, last_name=prenom)
            personnel.compte_utilisateur=user
            user.groups.set([gp,])
            permis=Permission.objects.all().filter(group=gp.id)
            for perm in permis:
                user.user_permissions.add(perm)
            personnel.save()
            mail(request, emailto=email , nom=nom, prenom=prenom, username=username, mdp=mdp)

            return redirect('gestschools:liste_personnel') 
        else:
            return render(request, 'gestschools/personnel.html', {'form': form})
    else:
        return render(request, 'gestschools/personnel.html', {'form': form})

def programme_trans(request):
    form = forms.Programme_transForm
    if request.method=='POST':
        form = forms.Programme_transForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestschools:liste_programme')
        else:
            return render(request, 'gestschools/Programme_trans.html', {'form': form})
    else:
        return render(request, 'gestschools/Programme_trans.html', {'form': form})

def bus(request):
    form = forms.BusForm
    if request.method=='POST':
        form = forms.BusForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('gestschools:bus')
        else:
            return render(request, 'gestschools/bus.html', {'form': form})
    else:
        return render(request, 'gestschools/bus.html', {'form': form})

def zone(request):
    form = forms.ZoneForm
    if request.method=='POST':
        form = forms.ZoneForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('gestschools:zone')
        else:
            return render(request, 'gestschools/zone.html', {'form': form})
    else:
        return render(request, 'gestschools/zone.html', {'form': form})

def niveau(request):
    form = forms.NiveauForm
    if request.method=='POST':
        form =forms.NiveauForm(request.POST)
        if form.is_valid(): 
            form.save(commit=True)
            return redirect('gestschools:niveau')
        else:
            return render(request, 'gestschools/niveau.html', {'form': form})
    else:
        return render(request, 'gestschools/niveau.html', {'form': form})
class liste_niveaux(generic.ListView):
    model = Niveau
    context_object_name = 'niveaux'
    template_name = 'liste_niveaux.html'

class NiveauDeleteView(BSModalDeleteView):
    model = Niveau
    template_name = 'gestschools/delete_niveaux.html'
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_niveaux')

class NiveauUpdateView(UpdateView):
    model = Niveau
    template_name = 'gestschools/update_niveaux.html'
    form_class = NiveauForm
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_niveaux')


# def registration_success(request):
    
#     return render(request, 'gestschools/registration_success.html')

# def registration_success_service(request):
    
#     return render(request, 'gestschools/registration_success_service.html')


def elevecon(request):
    form = forms.EleveconForm
    if request.method=='POST':
        form = forms.EleveconForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestschools:inscriptionCon')
        else:
            return render(request, 'gestschools/elevecon.html', {'form': form})
    else:
        return render(request, 'gestschools/elevecon.html', {'form': form})


class liste_elevecon(generic.ListView):
    model = Elevecon
    context_object_name = 'eleves'
    template_name = 'liste_elevecon.html'
def listeelevecon(request):
    eleves=Elevecon.objects.order_by('nomeelevec')
    return render(request, 'liste_elevecon.html', {'eleves': eleves})


class EleveconUpdateView(UpdateView):
    model = Elevecon
    template_name = 'gestschools/update_elevecon.html'
    form_class = EleveconForm
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_elevecon')

class EleveconDeleteView(BSModalDeleteView):
    model = Elevecon
    template_name = 'gestschools/delete_elevecon.html'
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_elevecon')


def concours(request):
    form = forms.ConcoursForm
    if request.method=='POST':
        form = forms.ConcoursForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestschools:liste_concours')
        else:
            return render(request, 'gestschools/concours.html', {'form': form})
    else:
        return render(request, 'gestschools/concours.html', {'form': form})


class liste_concours(generic.ListView):
    model = Concours
    context_object_name = 'concours'
    template_name = 'liste_concours.html'

class ConcoursUpdateView(UpdateView):
    model = Concours
    template_name = 'gestschools/update_concours.html'
    form_class = ConcoursForm
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_concours')

class ConcoursDeleteView(BSModalDeleteView):
    model = Concours
    template_name = 'gestschools/delete_concours.html'
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_concours')

def inscriptionCon(request):
    form = forms.InscriptionConForm
    if request.method=='POST':
        form = forms.InscriptionConForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestschools:liste_inscriptioncon')
        else:
            return render(request, 'gestschools/inscriptionCon.html', {'form': form})
    else:
        return render(request, 'gestschools/inscriptionCon.html', {'form': form})

class liste_inscriptioncon(generic.ListView):
    model = InscriptionCon
    context_object_name = 'inscriptions'
    template_name = 'liste_inscriptioncon.html'
def listeinscriptioncon(request):
    inscriptions=InscriptionCon.objects.order_by('elevecon__nomeelevec')
    return render(request, 'liste_inscriptioncon.html', {'inscriptions': inscriptions})

class InscriptionConUpdateView(UpdateView):
    model = InscriptionCon
    template_name = 'gestschools/update_inscriptioncon.html'
    form_class = InscriptionConForm
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_inscriptioncon')

class InscriptionConDeleteView(BSModalDeleteView):
    model = InscriptionCon
    template_name = 'gestschools/delete_inscriptionCon.html'
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_inscriptioncon')

def matiereconcours(request):
    form = forms.MatiereconcoursForm
    if request.method=='POST':
        form = forms.MatiereconcoursForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestschools:liste_matiereconcours')
        else:
            return render(request, 'gestschools/matiereconcours.html', {'form': form})
    else:
        return render(request, 'gestschools/matiereconcours.html', {'form': form})


class liste_matiereconcours(generic.ListView):
    model = Matiereconcours
    context_object_name = 'matieres'
    template_name = 'liste_matiereconcours.html'

class MatiereconcoursUpdateView(UpdateView):
    model = Matiereconcours
    template_name = 'gestschools/update_matiereconcours.html'
    form_class = MatiereconcoursForm
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_matiereconcours')

class MatiereconcoursDeleteView(BSModalDeleteView):
    model = Matiereconcours
    template_name = 'gestschools/delete_matiereconcours.html'
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_matiereconcours')
def programmation(request):
    form = forms.ProgrammationForm
    if request.method=='POST':
        form = forms.ProgrammationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('gestschools:programmation')
        else:
            return render(request, 'gestschools/programmation.html', {'form': form})
    else:
        return render(request, 'gestschools/programmation.html', {'form': form})
def jours(request):
    form = forms.JoursForm
    if request.method=='POST':
        form = forms.JoursForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('gestschools:jours')
        else:
            return render(request, 'gestschools/jours.html', {'form': form})
    else:
        return render(request, 'gestschools/jours.html', {'form': form})

# def liste_programmation(request):
# 	j = Jours.objects.all()
# 	p = Plage_horaire.objects.all()
# 	c = Programmation.objects.all()
# 	return render(request, 'liste_programmation.html', {'j': j, 'p': p})

def emploi_temps(request):
    form = forms.Emploi_tempsForm
    if request.method=='POST':
        form = forms.Emploi_tempsForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('gestschools:liste_emploi_temps')
        else:
            return render(request, 'gestschools/emploi_temps.html', {'form': form})
    else:
        return render(request, 'gestschools/emploi_temps.html', {'form': form})


def courslundi(request):
    form = forms.CoursLundiForm
    if request.method=='POST':
        form = forms.CoursLundiForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('gestschools:coursmardi')
        else:
            return render(request, 'gestschools/courslundi.html', {'form': form})
    else:
        return render(request, 'gestschools/courslundi.html', {'form': form})
def coursmardi(request):
    form = forms.CoursMardiForm
    if request.method=='POST':
        form = forms.CoursMardiForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('gestschools:coursmercredi')
        else:
            return render(request, 'gestschools/coursmardi.html', {'form': form})
    else:
        return render(request, 'gestschools/coursmardi.html', {'form': form})
def coursmercredi(request):
    form = forms.CoursMercrediForm
    if request.method=='POST':
        form = forms.CoursMercrediForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('gestschools:coursjeudi')
        else:
            return render(request, 'gestschools/coursmercredi.html', {'form': form})
    else:
        return render(request, 'gestschools/coursmercredi.html', {'form': form})
def coursjeudi(request):
    form = forms.CoursJeudiForm
    if request.method=='POST':
        form = forms.CoursJeudiForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('gestschools:coursvendredi')
        else:
            return render(request, 'gestschools/coursjeudi.html', {'form': form})
    else:
        return render(request, 'gestschools/coursjeudi.html', {'form': form})
def coursvendredi(request):
    form = forms.CoursVendrediForm
    if request.method=='POST':
        form = forms.CoursVendrediForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('gestschools:courssamedi')
        else:
            return render(request, 'gestschools/coursvendredi.html', {'form': form})
    else:
        return render(request, 'gestschools/coursvendredi.html', {'form': form})
def courssamedi(request):
    form = forms.CoursSamediForm
    if request.method=='POST':
        form = forms.CoursSamediForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('gestschools:emploi_temps')
        else:
            return render(request, 'gestschools/courssamedi.html', {'form': form})
    else:
        return render(request, 'gestschools/courssamedi.html', {'form': form})

class liste_eleverecruter(generic.ListView):
    model = Eleverecruter
    context_object_name = 'eleves'
    template_name = 'liste_eleverecruter.html'
    
def eleverecrutes(request):
    eleves=Eleverecruter.objects.all().order_by('elevecon__nomeelevec')
    return render(request, 'liste_eleverecruter.html', {'eleves': eleves})


def eleverecruter(request):
    form = forms.EleverecruterForm
    if request.method=='POST':
        form = forms.EleverecruterForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('gestschools:eleverecruter')
        else:
            return render(request, 'gestschools/eleverecruter.html', {'form': form})
    else:
        return render(request, 'gestschools/eleverecruter.html', {'form': form})


class EleverecruterUpdateView(UpdateView):
    model = Eleverecruter
    template_name = 'gestschools/update_eleverecruter.html'
    form_class = EleverecruterForm
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_eleverecruter')

class EleverecruterDeleteView(BSModalDeleteView):
    model = Eleverecruter
    template_name = 'gestschools/delete_eleverecruter.html'
    success_message = 'Suppression effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_eleverecruter')


def qualification(request):
    form = forms.QualificationForm
    if request.method=='POST':
        form = forms.QualificationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('gestschools:qualification')
        else:
            return render(request, 'gestschools/qualification.html', {'form': form})
    else:
        return render(request, 'gestschools/qualification.html', {'form': form})
def certificat(request):
    form = forms.CertificatForm
    if request.method=='POST':
        form = forms.CertificatForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('gestschools:liste_certificat')
        else:
            return render(request, 'gestschools/certificat.html', {'form': form})
    else:
        return render(request, 'gestschools/certificat.html', {'form': form})
class Liste_certificat(generic.ListView):
    model = Certificatsco
    context_object_name = 'certificats'
    template_name = 'liste_certificat.html'
def listecertificat(request):
    certificats=Certificatsco.objects.all().order_by('eleve__nom')
    return render(request, 'liste_certificat.html', {'certificats': certificats})

class CertificatUpdateView(UpdateView):
    model = Certificatsco
    template_name = 'gestschools/update_certificat.html'
    form_class = Affecter_classeForm
    success_url = reverse_lazy('gestschools:liste_certificat')

class CertificatDeleteView(BSModalDeleteView):
    model = Certificatsco
    template_name = 'gestschools/delete_certificat.html'
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_certificat')

class CertificatPDF(View):
   
  
    template_name = 'certificatPDF.html'
    def get(self, request, *args, **kwargs):
        template = get_template('gestschools/certificatPDF.html')
        certificats=Certificatsco.objects.all()
        e=Etablissement.objects.all()

        context = {
            
            "certificats":certificats,
            "e":e,
        }
        html= template.render(context)
        pdf = render_to_pdf('gestschools/certificatPDF.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Certificat de scolarité.pdf"
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found") 

def etablissement(request):
    form = forms.EtablissementForm
    
    if request.method=='POST':
        form = forms.EtablissementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestschools:etablissement')
        else:
            return render(request, 'gestschools/etablissement.html', {'form': form})
    else:            
        return render(request, 'gestschools/etablissement.html', {'form': form})

class Liste_etablissement(generic.ListView):
    model = Etablissement
    context_object_name = 'etablissements'
    template_name = 'liste_etablissement.html'
class EtablissementUpdateView(UpdateView):
    model = Etablissement
    template_name = 'gestschools/update_etablissement.html'
    form_class = EtablissementForm
    success_url = reverse_lazy('gestschools:liste_etablissement')

class EtablissementDeleteView(BSModalDeleteView):
    model = Etablissement
    template_name = 'gestschools/delete_etablissement.html'
    success_message = 'Opération effectuée avec sucès!!!.'
    success_url = reverse_lazy('gestschools:liste_etablissement')

def conseildiscipline(request):
    form = forms.ConseildisciplineForm
    
    if request.method=='POST':
        form = forms.ConseildisciplineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestschools:conseildiscipline')
        else:
            return render(request, 'gestschools/conseildiscipline.html', {'form': form})
    else:            
        return render(request, 'gestschools/conseildiscipline.html', {'form': form})
def decisionconseil(request):
    form = forms.DecisionconseilForm
    
    if request.method=='POST':
        form = forms.DecisionconseilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestschools:decisionconseil')
        else:
            return render(request, 'gestschools/decisionconseil.html', {'form': form})
    else:            
        return render(request, 'gestschools/decisionconseil.html', {'form': form})
def decisionfinalconseil(request):
    form = forms.DecisionfinalconseilForm
    
    if request.method=='POST':
        form = forms.DecisionfinalconseilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestschools:decisionfinalconseil')
        else:
            return render(request, 'gestschools/decisionfinalconseil.html', {'form': form})
    else:            
        return render(request, 'gestschools/decisionfinalconseil.html', {'form': form})
def statutenseignant(request):
    form = forms.StatutenseignantForm
    
    if request.method=='POST':
        form = forms.StatutenseignantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestschools:statutenseignant')
        else:
            return render(request, 'gestschools/statutenseignant.html', {'form': form})
    else:            
        return render(request, 'gestschools/statutenseignant.html', {'form': form})
def type_contrat(request):
    form = forms.Type_contratForm
    if request.method=='POST':
        form = forms.Type_contratForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestschools:type_contrat')
        else:
            return render(request, 'gestschools/type_contrat.html', {'form': form})
    else:            
        return render(request, 'gestschools/type_contrat.html', {'form': form})
