from django.urls import path,include
from gestschools import views
# from gestschools.views import RegistrationCreate, registration_success, registration_success_service
from django.contrib.auth.views import LoginView
from .views import GeneratePDF


#TEMPLATE TAGGING
app_name =  'gestschools'

urlpatterns= [

    path('signup/', views.signup, name='signup'),
    #path(r'login/', views.login, name='login'),
    path('gestschools/logout/', views.logout_view, name='logout'),

    path('pdf/', views.ServicePDF.as_view(), name='pdf'),
    path('Liste_des_eleves/', views.AffecterclassePDF.as_view(), name='affecte'),
    path('Liste_des_enseignants/', views.EnseignantPDF.as_view(), name='ens'),
    path('Liste_des_affectations/', views.AfectationPDF.as_view(), name='aff'),
    path('Liste_des_élèves/', views.ElevePDF.as_view(), name='el'),
    path('emplois de temps/', views.EmploiPDF.as_view(), name='em'),
    path('liste du personnel/', views.PersonnelPDF.as_view(), name='per'),
    path('programme de transport/', views.ProgrammePDF.as_view(), name='trans'),
    path('Statique des absences/', views.AbsencePDF.as_view(), name='ab'),

    
    path(r'login/', views.login_view, name='login'),
    path('lockscreen/', views.lockscreen, name='lockscreen'),
    path('user_view/', views.user_view, name='user_view'),
    path('menu/' ,views.menu, name='menu'),
    path('menueleve/' ,views.menueleve, name='menueleve'),
    path('enseignant/' ,views.enseignant, name='enseignant'),
    path('pays/' ,views.pays, name='pays'),
    path('cycle/' ,views.cycle, name='cycle' ),
    path('serie/' ,views.serie, name='serie' ),
    path('parents/' ,views.parents, name='parents' ),
    path('anneescolaire/' ,views.anneescolaire, name='anneescolaire' ),
    path('groupematiere/' ,views.groupematiere, name='groupematiere' ),    path('sequence/' ,views.sequence, name='sequence' ),
    path('programme/' ,views.programme, name='programme' ),
    path('trimestre/' ,views.trimestre, name='trimestre' ),
    path('sequence/' ,views.sequence, name='sequence' ),
    path('region/' ,views.region, name='region' ),
    path('departement/' ,views.departement, name='departement' ),    
    path('arrondissement/' ,views.arrondissement, name='arrondissement' ),    
    path('ville/' ,views.ville, name='ville' ),    
    path('affectation/' ,views.affectation, name='affectation' ),
    path('periodeeval/' ,views.periodeeval, name='periodeeval' ),
    path('affecter_classe/' ,views.affecter_classe, name='affecter_classe' ),
    path('preinscription/' ,views.preinscription, name='preinscription' ),
    path('absence/' ,views.absence, name='absence' ),
    path('etablissement/' ,views.etablissement, name='etablissement' ),
    path('ancienetablissement/' ,views.ancienetablissement, name='ancienetablissement' ),
    path('animateurpedagogique/' ,views.animateur_pedagogique, name='animateur_pedagogique' ),
    path('enseignant_titulaire/' ,views.enseignant_titulaire, name='enseignant_titulaire' ),
    path('evaluation/', views.evaluation, name='evaluation'),
    path('typefrais/', views.typefrais, name='typefrais'),
    path('fraispayer/', views.fraispayer, name='fraispayer'),
    path('service/', views.service, name='service'),
    path('personnel/', views.personnel, name='personnel'),
    path('programme_trans/', views.programme_trans, name='programme_trans'),
    path('bus/', views.bus, name='bus'),
    path('zone/', views.zone, name='zone'),

    path('evaluernote/', views.evaluernote, name='evaluernote'),

    path('liste_eleves/', views.listeeleves, name='liste_eleves'),
    path(r'update_eleve/?P<pk>\d+/', views.EleveUpdateView.as_view(), name='update_eleve'),
    path('delete/<int:pk>/', views.EleveDeleteView.as_view(), name='delete_eleve'),
   
    path('liste_personnel/', views.liste_personnel.as_view(), name='liste_personnel'),
    path(r'update_personnel/?P<pk>\d+/', views.PersonnelUpdateView.as_view(), name='update_personnel'),
    path('delete_personnel/<int:pk>/', views.PersonnelDeleteView.as_view(), name='delete_personnel'),
    
    path('liste_service/', views.liste_service.as_view(), name='liste_service'),
    path('delete_service/<int:pk>/', views.ServiceDeleteView.as_view(), name='delete_service'),

    path('liste_programme/', views.liste_programme.as_view(), name='liste_programme'),
    path('delete_programme/<int:pk>/', views.ProgrammeDeleteView.as_view(), name='delete_programme'),


    path('liste_titulaires/', views.listetitulaires, name='liste_titulaires'),
    path(r'update_titulaire/?P<pk>\d+/', views.TitulaireUpdateView.as_view(), name='update_titulaire'),
    path('delete_titulaire/<int:pk>/', views.TitulaireDeleteView.as_view(), name='delete_titulaire'),

    path('deleteevaluation/<int:pk>/', views.EvaluationDeleteView.as_view(), name='delete_evaluation'),
    path('liste_evaluations/', views.liste_evaluations.as_view(), name='liste_evaluations'),
    
    path('deleteabsence/<int:pk>', views.AbsenceDeleteView.as_view(), name='delete_absence'),
    path(r'updateabsence/?P<pk>\d+/', views.AbsenceUpdateView.as_view(), name='update_absence'),
    path('liste_absences/', views.listeabsences, name='liste_absences'),


    path('deletepreinscription/<int:pk>', views.PreinscriptionDeleteView.as_view(), name='delete_preinscription'),
    path('liste_preinscriptions/', views.liste_preinscriptions.as_view(), name='liste_preinscriptions'),

    path('liste_affectations/', views.listeaffectations, name='liste_affectations'),
    path('delete_affectation/<int:pk>', views.AffectationDeleteView.as_view(), name='delete_affectation'),
    path(r'update_affectation/?P<pk>\d+/', views.AffectationUpdateView.as_view(), name='update_affectation'),

    path('liste_enseignants/', views.listeenseignants, name='liste_enseignants'),
    path(r'update_enseignant/?P<pk>\d+/', views.EnseignantUpdateView.as_view(), name='update_enseignant'),
    path('delete_enseignant/<int:pk>/', views.EnseignantDeleteView.as_view(), name='delete_enseignant'),

    path('matiere/' ,views.matiere, name='matiere' ),    path('sequence/' ,views.sequence, name='sequence' ),
    path('liste_matiere/', views.liste_matiere.as_view(), name='liste_matiere'),
    path(r'deletematiere/<int:pk>/', views.MatiereDeleteView.as_view(), name='delete_matiere'),
  
    path('discipline_competence/' ,views.discipline_competence, name='discipline_competence' ),
    path(r'deletediscipline/<int:pk>/', views.Discipline_competenceDeleteView.as_view(), name='delete_discipline'),
    path('liste_disciplines/',views.liste_disciplines.as_view(), name='liste_disciplines'),
  
    path('classe/' ,views.classe, name='classe' ),
    path('liste_classes/', views.liste_classes.as_view(), name='liste_classes'),
    path(r'deleteclasse/<int:pk>/', views.ClasseDeleteView.as_view(), name='delete_classe'),
    
    path('niveau/' ,views.niveau, name='niveau' ),
    path('liste_niveaux/', views.liste_niveaux.as_view(), name='liste_niveaux'),
    path(r'delete_niveau/<int:pk>/', views.NiveauDeleteView.as_view(), name='delete_niveaux'),
    path(r'update_niveau/?P<pk>\d+/', views.NiveauUpdateView.as_view(), name='update_niveaux'),

    path('eleveconcours/', views.elevecon, name='elevecon'),
    path('liste_elevecon/', views.listeelevecon, name='liste_elevecon'),
    path(r'update_elevecon/?P<pk>\d+/', views.EleveconUpdateView.as_view(), name='update_elevecon'),
    path(r'delete_enseignant/<int:pk>/', views.EleveconDeleteView.as_view(), name='delete_elevecon'),

    path('concours/', views.concours, name='concours'),
    path('liste_concours/', views.liste_concours.as_view(), name='liste_concours'),
    path(r'update_concours/?P<pk>\d+/', views.ConcoursUpdateView.as_view(), name='update_concours'),
    path(r'delete_concours/<int:pk>/', views.ConcoursDeleteView.as_view(), name='delete_concours'),

    path('inscriptionCon/', views.inscriptionCon, name='inscriptionCon'),
    path('liste_inscriptioncon/', views.listeinscriptioncon, name='liste_inscriptioncon'),
    path(r'update_inscriptioncon/?P<pk>\d+/', views.InscriptionConUpdateView.as_view(), name='update_inscriptioncon'),
    path(r'delete_inscriptionCon/<int:pk>/', views.InscriptionConDeleteView.as_view(), name='delete_inscriptionCon'),

    path('matiereconcours/', views.matiereconcours, name='matiereconcours'),
    path('liste_matiereconcours/', views.liste_matiereconcours.as_view(), name='liste_matiereconcours'),
    path(r'update_matiereconcours/?P<pk>\d+/', views.MatiereconcoursUpdateView.as_view(), name='update_matiereconcours'),
    path(r'delete_matiereconcours/<int:pk>/', views.MatiereconcoursDeleteView.as_view(), name='delete_matiereconcours'),

    path('admin/', views.admin, name='admin'),
    path('liste_admin/', views.listeadmin, name='liste_admin'),
    path(r'update_admin/?P<pk>\d+/', views.AdminUpdateView.as_view(), name='update_admin'),
    path(r'delete_admin/<int:pk>/', views.AdminDeleteView.as_view(), name='delete_admin'),

    path('liste_affecterclasse/', views.listeaffecterclasse, name='liste_affecterclasse'),
    path(r'update_affecter_classe/?P<pk>\d+/', views.AffecterUpdateView.as_view(), name='update_affecter_classe'),
    path(r'delete_affecter_classe/<int:pk>/', views.AffecterDeleteView.as_view(), name='delete_affecter_classe'),

    path('emploi_temps/' ,views.emploi_temps, name='emploi_temps' ),
    path('liste_emploi_temps/', views.liste_emploi_temps.as_view(), name='liste_emploi_temps'),
    path(r'update_emploi_temps/?P<pk>\d+/', views.Emploi_tempsUpdateView.as_view(), name='update_emploi_temps'),
    path(r'delete_emploi_temps/<int:pk>/', views.Emploi_tempsDeleteView.as_view(), name='delete_emploi_temps'),

    
    path('courslundi/' ,views.courslundi, name='courslundi' ),
    path('coursmardi/' ,views.coursmardi, name='coursmardi' ),
    path('coursmercredi/' ,views.coursmercredi, name='coursmercredi' ),
    path('coursjeudi/' ,views.coursjeudi, name='coursjeudi' ),
    path('coursvendredi/' ,views.coursvendredi, name='coursvendredi' ),
    path('courssamedi/' ,views.courssamedi, name='courssamedi' ),


    path('liste_evaluernote/', views.liste_evaluernote.as_view(), name='liste_evaluernote'),
    path(r'update_evaluernote/?P<pk>\d+/', views.EvaluernoteUpdateView.as_view(), name='update_evaluernote'),
    path(r'delete_evaluernote/<int:pk>/', views.EvaluernoteDeleteView.as_view(), name='delete_evaluernote'),

    path('moyennesequentiel/' ,views.moyennesequentiel, name='moyennesequentiel' ),


    # path('jours/' ,views.jours, name='jours' ),
    # path('programmation/' ,views.programmation, name='programmation' ),
    # path('liste_programmation/', views.liste_programmation, name='liste_programmation'),

    path('eleverecruter/' ,views.eleverecruter, name='eleverecruter' ),
    path('liste_eleverecruter/', views.eleverecrutes, name='liste_eleverecruter'),

    # path('liste_eleverecruter/', views.listeeleverecruter, name='liste_eleverecruter'),
    path(r'update_eleverecruter/?P<pk>\d+/', views.EleverecruterUpdateView.as_view(), name='update_eleverecruter'),
    path(r'delete_eleverecruter/<int:pk>/', views.EleverecruterDeleteView.as_view(), name='delete_eleverecruter'),

    path('qualification/' ,views.qualification, name='qualification' ),
   
    path('certificat/' ,views.certificat, name='certificat' ),
    path('liste_certificat/', views.listecertificat, name='liste_certificat'),
    path(r'update_certificat/?P<pk>\d+/', views.CertificatUpdateView.as_view(), name='update_certificat'),
    path(r'delete_certificat/<int:pk>/', views.CertificatDeleteView.as_view(), name='delete_certificat'),
    path(r'Certificat de scolasité/<int:pk>/', views.CertificatPDF.as_view(), name='certificatPDF'),

    path('liste_etablissement/', views.Liste_etablissement.as_view(), name='liste_etablissement'),
    path(r'update_etablissement/?P<pk>\d+/', views.EtablissementUpdateView.as_view(), name='update_etablissement'),
    path(r'delete_etablissement/<int:pk>/', views.EtablissementDeleteView.as_view(), name='delete_etablissement'),

    path('type_contrat/' ,views.type_contrat, name='type_contrat' ),
    path('statutenseignant/' ,views.statutenseignant, name='statutenseignant' ),
    path('decisionfinalconseil/' ,views.decisionfinalconseil, name='decisionfinalconseil' ),
    path('decisionconseil/' ,views.decisionconseil, name='decisionconseil' ),
    path('conseildiscipline/' ,views.conseildiscipline, name='conseildiscipline' ),

]
