from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.

class Personne(models.Model):
    nom=models.CharField("Nom*", max_length=100 )
    prenom=models.CharField("Prénom*", max_length=100 )
    date_naiss=models.CharField("Date de Naissance*", max_length=100 )
    lieu_naiss=models.CharField("Lieu de naissance*",max_length=100)
    email=models.EmailField("E-mail*")
    telephone=models.CharField( "Téléphone*", validators=[
        RegexValidator(
            regex="^6[5-9]([0-9]){7}$",
            message="Entrer un numéro de telephone valide"
        ) 
    ], max_length=9)
    compte_utilisateur=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract=True

class Administrateur(Personne):
    pass

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.png', '.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Please select a valid image (.jpg,.png,.jpeg)')


class Pays(models.Model):
    codepays = models.CharField(max_length=20, verbose_name="Code pays")
    libellepayslng1 = models.CharField(max_length=60, verbose_name="Libellé1")
    libellepayslng2 = models.CharField(max_length=60, verbose_name="Libellé2")
    devisepayslng1 = models.CharField(max_length=60, verbose_name="Devise1",null=True)
    devisepayslng2 = models.CharField(max_length=60, verbose_name="Devise2",null=True)
    monnaiepays = models.CharField(max_length=60, verbose_name="Monnaie",null=True)

    def __str__(self):
        return self.libellepayslng1

class Region(models.Model):
    
    pays = models.ForeignKey(Pays, on_delete=models.CASCADE,verbose_name="Pays")
    codeRegion = models.CharField(max_length=20, verbose_name="code région")
    libelleRegionlng1 = models.CharField(max_length=60, verbose_name="Libellé région1")
    libelleRegionlng2 = models.CharField(max_length=60, verbose_name="Libellé région2")
    libelledelegationlng1 = models.CharField(max_length=60, verbose_name="Libellé délégation régional1")
    libelledelegationlng2 = models.CharField(max_length=60, verbose_name="Libellé délégation régional2")
   

    def __str__(self):
        return self.libelledelegationlng1

class Departementgeo(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE,verbose_name="Region*")
    codedepartementgeo = models.CharField(max_length=20, verbose_name="Code département",null=True, blank=True)
    libelledepartlng1 = models.CharField(max_length=60, verbose_name="Libellé département1*")
    libelledepartlng2 = models.CharField(max_length=60, verbose_name="Libellé département2",null=True, blank=True)
    libelledelegationdeparlng1 = models.CharField(max_length=60, verbose_name="Libellé délégation départemental1*")
    libelledelegationdeparlng2 = models.CharField(max_length=60, verbose_name="Libellé délégation départemental2",null=True,blank=True)
   
    def __str__(self):
        return self.libelledepartlng1

class Arrondissement(models.Model):
    departement = models.ForeignKey(Departementgeo, on_delete=models.CASCADE,verbose_name="Departement*")
    codearrondissement = models.CharField(max_length=20, verbose_name="Code arrondissement",null=True, blank=True)
    libellearronlng1 = models.CharField(max_length=60, verbose_name="Libellé1*")
    libellearronlng2 = models.CharField(max_length=60, verbose_name="Libellé2",null=True, blank=True)
    def __str__(self):
        return self.libellearronlng1

class Ville(models.Model):
    arrondissement = models.ForeignKey(Arrondissement, on_delete=models.CASCADE,verbose_name="Arrondissement*")
    codeville = models.CharField(max_length=20, verbose_name="Code ville",null=True, blank=True)
    libellevillelng1 = models.CharField(max_length=60, verbose_name="Libellé1*")
    libellevillelng2 = models.CharField(max_length=60, verbose_name="Libellé2",null=True,blank=True)
    def __str__(self):
        return self.libellevillelng1

class Parents(models.Model):
    #idparents = models.AutoField(primary_key=True, default=0)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE,verbose_name="Ville*")
    codeparents = models.CharField(max_length=30,verbose_name="Code parent",blank=True)
    nompere = models.CharField(max_length=60,verbose_name="Nom père*")
    telpere = models.CharField(max_length=30, null=True,verbose_name="Tel père*")
    professionpere = models.CharField(max_length=30, null=True,verbose_name="Profession père",blank=True)
    nommere = models.CharField(max_length=30,verbose_name="Nom mère*")
    telmere = models.CharField(max_length=30, null=True,verbose_name="Tel mère",blank=True)
    professionmere = models.CharField(max_length=20, null=True,verbose_name="Profession mère", blank=True)
    nomtuteur = models.CharField(max_length=20,verbose_name="Nom tuteur",blank=True)
    teltuteur = models.CharField(max_length=90,verbose_name="Tel tuteur",blank=True)
    emailparent = models.CharField(max_length=50, null=True,verbose_name="Email parents", blank=True)
    bpparent = models.CharField(max_length=30,verbose_name="BP parents", blank=True)
    professiontuteur = models.CharField(max_length=90, null=True,verbose_name="Profession tuteur", blank=True)
    residencetuteur = models.CharField(max_length=90, null=True,verbose_name="Residence tuteur" ,blank=True)
    emailtuteur = models.CharField(max_length=90, null=True,verbose_name="Email tuteur",blank=True)
    residenceparents = models.CharField(max_length=90, null=True,verbose_name="Residence parents", blank=True)
    
    def __str__(self):
        return self.nompere
sexe=(("M","Masculin"),("F","Feminin"))
civ=(("M.","Mr."),("Mme.","Mme."),("Mlle.","Mlle."))
handicap=(("Oui","Oui"),("Non","Non"))
class Eleve(models.Model):
   
    parents = models.ForeignKey(Parents, on_delete=models.CASCADE,verbose_name="Parent  ")   
    #photo = models.FileField(validators=[validate_file_extension],verbose_name="Image ",blank=True)
    codeeleve = models.CharField(max_length=30, verbose_name="Code de l'élève" , blank=True)
    matriculeeleve = models.CharField(max_length=30 , verbose_name="Matricule",unique=True)
    civilite = models.CharField(max_length=30, null=True, verbose_name="Civilité",choices=civ)
    nom = models.CharField(max_length=30, verbose_name="Nom ")
    prenom = models.CharField(max_length=60, null=True, verbose_name="Prenom",blank=True)
    lieunaiss = models.CharField("Lieu de naissance",max_length=30, null=True)
    datenaissel = models.CharField(max_length=20,verbose_name="Date de naissance")
    sexe = models.CharField(max_length=20,choices=sexe,verbose_name="Sexe")
    nationalite = models.CharField(max_length=30, null=True, verbose_name="Nationalité ")
    emaileleve = models.CharField(max_length=50, verbose_name="Email ",blank=True)
    teleeleve = models.CharField(max_length=9, null=True, verbose_name="Téléphone ",blank=True,
    validators= [RegexValidator(regex="^6[5-9]([0-9]){7}$",
    message="Entre un numéro valide")
    ])
    adresseeleve = models.CharField(max_length=90, null=True, verbose_name="Adresse ")
    handicape = models.CharField(max_length=30, null=True,choices=handicap ,verbose_name="Handicape ")
    langueofficielle = models.CharField(max_length=90, null=True, verbose_name="Langue officielle ")
    numeroinscription = models.CharField(max_length=30, null=True ,verbose_name="Numero d'inscription ") 
    modeadmission = models.CharField(max_length=90, null=True, verbose_name="Mode d'admission ",blank=True)
    
    def __str__(self):
        
        return '%s %s' % (self.nom, self.prenom)

class Discipline_competence(models.Model):
    codediscipline_compe = models.CharField(max_length=60, verbose_name="Code discipline")
    libellediscipline_comlng = models.CharField(max_length=60, verbose_name="Libellé")

    def __str__(self):
        return self.libellediscipline_comlng 

class Qualification(models.Model):
    codeq = models.CharField(max_length=60, verbose_name="Code qualification")
    libellequalif = models.CharField(max_length=60, verbose_name="Libellé")
    def __str__(self):
        return self.libellequalif 
class Type_contrat(models.Model):
    codetype_contrat = models.CharField(max_length=60, verbose_name="Code type contrat", null=True)
    libelletype_contrat = models.CharField(max_length=60, verbose_name="Libellé type contrat*")
    def __str__(self):
        return self.libelletype_contrat 
class Statutenseignant(models.Model):
    codestatut = models.CharField(max_length=60, verbose_name="Code statut", null=True)
    libellestatutlng1 = models.CharField(max_length=60, verbose_name="Libellé statut1*")
    libellestatutlng2 = models.CharField(max_length=60, verbose_name="Libellé statut2", null=True,blank=True)
    def __str__(self):
        return self.libellestatutlng1 


class Enseignant(Personne):
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE,verbose_name="Qualification*", null=True)
    statutenseignant = models.ForeignKey(Statutenseignant, on_delete=models.CASCADE,verbose_name="Statut*", null=True)
    discipline = models.ForeignKey(Discipline_competence, on_delete=models.CASCADE,verbose_name="Discipline*")
    type_contrat = models.ForeignKey(Type_contrat, on_delete=models.CASCADE,verbose_name="Type de contrat*", null=True)
    matriculeens = models.CharField(max_length=30, verbose_name="Matricule", null=True,blank=True)
    civilite = models.CharField(max_length=30, null=True, verbose_name="Civilité*",choices=civ)
    sexe = models.CharField(max_length=20,choices=sexe,verbose_name="Sexe*")
    profession = models.CharField(max_length=90, verbose_name="Profession*")
    nationalite = models.CharField(max_length=30, verbose_name="Nationalité*")
    adresseens = models.CharField(max_length=90, null=True, verbose_name="Adresse*")
    villeresidence = models.CharField(max_length=90, null=True, verbose_name="Ville de residence*")
    langueofficielle = models.CharField(max_length=90, null=True, verbose_name="Langue officielle*")
    villenaiss = models.CharField(max_length=50, verbose_name="Ville de naissance")
    fax = models.CharField(max_length=30, null=True, verbose_name="  Fax         ")
    regionorigine = models.CharField(max_length=50, null=True, verbose_name="Région d'origine*")
    departementorigine = models.CharField(max_length=250, null=True, verbose_name="Département d'origine")
    diplomeacademique = models.CharField(max_length=250, verbose_name="Diplome académique*")
    diplomeprof = models.CharField(max_length=250, null=True, verbose_name="Diplome professionnel")
    dataentreefonctionpublique = models.CharField(max_length=30,null=True,verbose_name="Date d'entrée en fonction publique")
    datemiseretraite = models.CharField("Date de mise en retraite",max_length=30,null=True)

    def __str__(self):
        return '%s %s' % (self.nom, self.prenom)
class Cycle(models.Model):
    codecycle = models.CharField(max_length=10,verbose_name="Code cycle")
    libellecyclelng1 = models.CharField(max_length=60,verbose_name="Libellé cycle1")
    def __str__(self):
        return self.libellecyclelng1 
class Section(models.Model):
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE,verbose_name="Cycle", null=True)
    codesection = models.CharField(max_length=30,verbose_name="Code section")
    libellesectionlng1 = models.CharField(max_length=60,verbose_name="Libellé section1")
    libellesectionlng2 = models.CharField(max_length=60,verbose_name="Libellé section2")
    def __str__(self):
        return self.libellesectionlng1

class Niveau(models.Model):
    codeniveau = models.CharField(max_length=30, verbose_name="Code du niveau")
    libelleniveau = models.CharField(max_length=60, verbose_name="Libellé niveau")
    diplomant = models.IntegerField(verbose_name="Diplomant")
    bloquant = models.IntegerField(verbose_name="Bloquant")

    def __str__(self):
        return self.libelleniveau 
class Serie(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE,verbose_name="Section", null=True)
    codeserie = models.CharField(max_length=30,verbose_name="Code série")
    libelleserielng1 = models.CharField(max_length=60,verbose_name="Libellé")

    def __str__(self):
        return self.libelleserielng1

class Classe(models.Model):

    serie = models.ForeignKey(Serie, on_delete=models.CASCADE,verbose_name="Série", null=True)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE,verbose_name="Niveau", null=True)
    codeclasse = models.CharField(max_length=10,verbose_name="Code classe")
    libelleclasse = models.CharField(max_length=60,verbose_name="Libellé")
    effectif = models.CharField(max_length=30,verbose_name="Effectif")

    def __str__(self):
        return self.libelleclasse 




# ceci est un model test

#class Person(models.Model):
   # name = models.CharField(max_length=130)
   # email = models.EmailField(blank=True)
   # job_title = models.CharField(max_length=30, blank=True)
   # bio = models.TextField(blank=True)

    

class Anneescolaire(models.Model):
   
    codeanneescolaire = models.CharField(max_length=10, verbose_name="Code année scolaire")
    libelleannee = models.CharField(max_length=60, verbose_name="Libellé année scolaire")
    datedebut = models.CharField(verbose_name="Date de début",max_length=60)
    datefin = models.CharField(verbose_name="Date de fin",max_length=60)
    encours = models.IntegerField(verbose_name="Encours")
    

    def __str__(self):
        return self.libelleannee

codetrim=(("1er Trim","1er Trim"),("2e Trim","2e Trim"),("3e Trim","3e Trim"))
ordretrim=(("1","1"),("2","2"),("3","3"))
class Trimestre(models.Model):
   
    codetrimestre = models.CharField(max_length=10, verbose_name="Code trimestre", choices=codetrim)
    libelletrimestre = models.CharField(max_length=60,verbose_name="Libellé trimestre" )
    ordretrim = models.IntegerField(verbose_name="Ordre trimestre")
    

    def __str__(self):
        return self.libelletrimestre 

codeseq=(("1seq","1seq"),("2seq","2seq"),("3seq","3seq"),("4seq","4seq"),("5seq","5seq"),("6seq","6seq"))
class Sequence(models.Model):
   
    trimestre = models.ForeignKey(Trimestre, on_delete=models.CASCADE,verbose_name="Trimestre")
    anneescolaire = models.ForeignKey(Anneescolaire, on_delete=models.CASCADE,verbose_name="Année scolaire")
    codesequence = models.CharField(max_length=10, verbose_name="Code Séquence", choices=codeseq)
    libelleseq = models.CharField(max_length=60, verbose_name="Libellé séquence")
    datedebut = models.CharField(max_length=60,verbose_name="Date de début")
    datefin = models.CharField(max_length=60,verbose_name="Date de fin")
    

    def __str__(self):
        return self.libelleseq

   
class Programme(models.Model):
   
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE,verbose_name="Niveau")
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE,verbose_name="Série", null=True)
    codeprogramme = models.CharField(max_length=60, verbose_name="Code programme", null=True)
    libelleprogramme = models.CharField(max_length=60, verbose_name="Libellé programme")
    
    def __str__(self):
        return self.libelleprogramme

class Groupematiere(models.Model):
   
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE,verbose_name="Programme")
    codegroupematiere = models.CharField(max_length=60, verbose_name="Code groupe matière")
    libellegroupematiere = models.CharField(max_length=60, verbose_name="Libellé groupe matiere")
    
    

    def __str__(self):
        return '%s %s' % (self.libellegroupematiere,self.programme)
class Matiere(models.Model):
   
    groupematiere = models.ForeignKey(Groupematiere, on_delete=models.CASCADE,verbose_name="Groupe matière")
    libellematiere = models.CharField(max_length=100, verbose_name="Libellé  matiere")
    coef = models.IntegerField(verbose_name="Coef")

    def __str__(self):
        return self.libellematiere



class Periodeeval(models.Model):
   
    libelleperiode = models.CharField(max_length=100, verbose_name="Libellé Période")
    datedebut = models.CharField(max_length=100,verbose_name="Date de début")
    datefin = models.CharField(max_length=100,verbose_name="Date de fin")
    

    def __str__(self):
        return self.libelleperiode

class Evaluation(models.Model):
   
    sequence = models.ForeignKey(Sequence, on_delete=models.CASCADE,verbose_name="Séquence")
    periodeeval = models.ForeignKey(Periodeeval, on_delete=models.CASCADE,verbose_name="Période évaluation",null=True, blank=True)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE,verbose_name="Classe")
    anneescolaire = models.ForeignKey(Anneescolaire, on_delete=models.CASCADE,verbose_name="Année scolaire")
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE,verbose_name="Matière")
    codeevaluation = models.CharField(max_length=20, verbose_name="Code évaluation", null=True,blank=True)
    dateeval = models.CharField(max_length=20,verbose_name="Date de l'évaluation")

    def __str__(self):
        return '%s' % (self.matiere)

class Evaluernote(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE,verbose_name="Elève")
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE,verbose_name="Evaluation")
    note = models.FloatField(verbose_name="Note",default=0.000 ,null=True)
    def __str__(self):
        return '%s' % (self.note)

    
class Affectation(models.Model):
   
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE,verbose_name="Enseignant")
    anneescolaire = models.ForeignKey(Anneescolaire, on_delete=models.CASCADE,verbose_name="Année scolaire")
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE,verbose_name="Matière")
    codeaffectation = models.CharField(max_length=20, verbose_name="Code affectation", null=True)

    def __str__(self):
        return '%s ' % (self.matiere)


class Moyennesequentiel(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE,verbose_name="Elève")
    sequence = models.ForeignKey(Sequence, on_delete=models.CASCADE,verbose_name="Séquence")
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE,verbose_name="Classe")
    anneescolaire = models.ForeignKey(Anneescolaire, on_delete=models.CASCADE,verbose_name="Année scolaire")
    absence = models.CharField(max_length=30, null=True, verbose_name="Absence",blank=True)
    decisionseq = models.CharField(max_length=255, null=True, verbose_name="Décision séquence",blank=True)
    moyenneseq = models.CharField(max_length=255, null=True, verbose_name="Moyenne séquence")
    listematieremauvais = models.CharField(max_length=255,null=True,verbose_name="Liste matière mauvaise", blank=True)
    rangs = models.CharField(max_length=20,verbose_name="Rangs")
    moyennepremier = models.CharField(max_length=30, verbose_name="Moyenne première")
    moyennedernier = models.CharField(max_length=30, verbose_name="Moyenne dernière")
    appreciationtravail = models.CharField(max_length=255, verbose_name="Appréciation du travail",null=True, blank=True)
    appreciationconduite = models.CharField(max_length=255, verbose_name="Appréciation conduite",null=True, blank=True)
    moyennegeneraleclasse = models.CharField(max_length=90, verbose_name="Moyenne générale de la classe")
    tableauhonneur = models.CharField(max_length=20, verbose_name="Tableau d'honneur",null=True, blank=True)
    encouragements = models.CharField(max_length=20, null=True, verbose_name="Encouragements", blank=True)
    felicitation = models.CharField(max_length=20, verbose_name="Félicitation",null=True, blank=True)
    avertissementtravail = models.CharField(max_length=20,  verbose_name="Avertissement travail",null=True, blank=True)
    avertissementconduite = models.CharField(max_length=20, verbose_name="Avertissement conduite",null=True, blank=True)
    blametravail = models.CharField(max_length=20, verbose_name="Blame travail",null=True, blank=True)
    blameconduite = models.CharField(max_length=20, verbose_name="Blame conduite",null=True, blank=True)
    exclusions = models.CharField(max_length=20, verbose_name="Exclusions",null=True, blank=True)



class Absence(models.Model):
   
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE,verbose_name="Elève",null=True)
    sequence = models.ForeignKey(Sequence, on_delete=models.CASCADE,verbose_name="Séquence",null=True)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE,verbose_name="Classe")
    codeeabcence = models.CharField(max_length=20, verbose_name="Code absence", null=True,blank=True)
    justifier = models.IntegerField(verbose_name="Justifier", null=True, default=0)
    nonjustifier = models.IntegerField(verbose_name="Non justifier", null=True,default=0)
    
    def __str__(self):
        return self.nonjustifier



class Affecter_classe(models.Model):
   
    anneescolaire = models.ForeignKey(Anneescolaire, on_delete=models.CASCADE,verbose_name="Année scolaire")
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE,verbose_name="Elève",null=True)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE,verbose_name="Classe")
    codeaffecter_classe = models.CharField(max_length=30, verbose_name="Code d'affectation", null=True, blank=True)
    inscrit = models.SmallIntegerField(verbose_name="Inscrit", null=True,default=0)
    paye = models.SmallIntegerField(verbose_name="Paye", null=True,default=0)
    numrecu = models.CharField(max_length=100, verbose_name="Numéro recu", null=True,default=0, blank=True)

    def __str__(self):
        return ' %s' % (self.eleve)

class Preinscription(models.Model):
   
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE,verbose_name="Classe")
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE,verbose_name="Elève",null=True)
    anneescolaire = models.ForeignKey(Anneescolaire, on_delete=models.CASCADE,verbose_name="Année scolaire")
    codepreinscription = models.CharField(max_length=30, verbose_name="Code préinscription", null=True, blank=True)
    elligibilite = models.SmallIntegerField(verbose_name="Elligibilité", null=True,default=0)
    redouble = models.SmallIntegerField(verbose_name="Redouble", null=True,default=0)

    def __str__(self):
        return self.codepreinscription


class Plage_horaire(models.Model):
   
    codeplage_horaire = models.CharField(max_length=30, verbose_name="Code plage horaire", null=True)
    libelleplage1 = models.CharField(max_length=30, verbose_name="Libellé plage1", null=True)
    libelleplage2  = models.CharField(max_length=30, verbose_name="Libellé plage2", null=True,default="")

    def __str__(self):
        return self.libelleplage1
class CoursLundi(models.Model):
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE,verbose_name="Programme",null=True)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE,verbose_name="Matière",blank=True)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE,verbose_name="Classe",blank=True)

    def __str__(self):
        return ' %s %s' % (self.matiere, self.classe)
class CoursMardi(models.Model):
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE,verbose_name="Matière",blank=True)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE,verbose_name="Classe",blank=True)

    def __str__(self):
        return ' %s %s' % (self.matiere, self.classe)
class CoursMercredi(models.Model):
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE,verbose_name="Matière",blank=True)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE,verbose_name="Classe",blank=True)

    def __str__(self):
        return ' %s %s' % (self.matiere, self.classe)
class CoursJeudi(models.Model):
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE,verbose_name="Matière",blank=True)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE,verbose_name="Classe",blank=True)

    def __str__(self):
        return ' %s %s' % (self.matiere, self.classe)
class CoursVendredi(models.Model):
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE,verbose_name="Matière",blank=True)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE,verbose_name="Classe",blank=True)

    def __str__(self):
        return ' %s %s' % (self.matiere, self.classe)
class CoursSamedi(models.Model):
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE,verbose_name="Matière",blank=True)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE,verbose_name="Classe",blank=True)

    def __str__(self):
        return ' %s %s' % (self.matiere, self.classe)


class Emploi_temps(models.Model):
   
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE,verbose_name="Programme")
    plage_horaire = models.ForeignKey(Plage_horaire, on_delete=models.CASCADE,verbose_name="Plage_horaire")
    courslundi = models.ForeignKey(CoursLundi, on_delete=models.CASCADE,verbose_name="Cours Lundi",null=True,blank=True)
    coursmardi = models.ForeignKey(CoursMardi, on_delete=models.CASCADE,verbose_name="Cours Mardi",null=True,blank=True)
    coursmercredi = models.ForeignKey(CoursMercredi, on_delete=models.CASCADE,verbose_name="Cours Mercredi",null=True,blank=True)
    coursjeudi = models.ForeignKey(CoursJeudi, on_delete=models.CASCADE,verbose_name="Cours Jeudi",null=True,blank=True)
    coursvendredi = models.ForeignKey(CoursVendredi, on_delete=models.CASCADE,verbose_name="Cours Vendredi",null=True,blank=True)
    courssamedi = models.ForeignKey(CoursSamedi, on_delete=models.CASCADE,verbose_name="Cours Samedi",null=True,blank=True)
    duree = models.CharField(max_length=20,verbose_name="Durée",null=True,blank=True)
    codeemploi = models.CharField(max_length=20,verbose_name="Code emploi temps",null=True,blank=True, unique=True)

  

class Jours(models.Model):
    codejour = models.CharField(max_length=20,verbose_name="Code jours",null=True,blank=True)
    libellejourlng1 = models.CharField(max_length=20,verbose_name="Libellé jours1",null=True)
    libellejourlng2 = models.CharField(max_length=20,verbose_name="Libellé jours2",null=True,blank=True)
    def __str__(self):
        return self.libellejourlng1

class Programmation(models.Model):
   
    jours = models.ForeignKey(Jours, on_delete=models.CASCADE,verbose_name="Jours")
    affectation = models.ForeignKey(Affectation, on_delete=models.CASCADE,verbose_name="Affectation",null=True,blank=True)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE,verbose_name="Classe",null=True)
    plage_horaire = models.ForeignKey(Plage_horaire, on_delete=models.CASCADE,verbose_name="Plage horaire",null=True)
    codeprogrammation = models.CharField(max_length=20,verbose_name="Code programmation",null=True,blank=True)
  


class Etablissement(models.Model):
   
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE,verbose_name="Ville  ")   
    #photo = models.FileField(validators=[validate_file_extension],verbose_name="Image ",blank=True)
    codeetablissement = models.CharField(max_length=30, verbose_name="Code établissement")
    sigleetablissement = models.CharField(max_length=50 , verbose_name="Sigle établissement",unique=True)
    devise = models.CharField(max_length=50, null=True, verbose_name="Devise")
    libelleetablng1 = models.CharField(max_length=100, verbose_name="Libellé établissement langue1 ")
    libelleetablng2 = models.CharField(max_length=100, null=True, verbose_name="Libellé établissement langue2")
    logo = models.FileField(validators=[validate_file_extension],verbose_name="Logo",null=True,blank=True)
    email = models.CharField(max_length=50,verbose_name="Email")
    bp = models.CharField(max_length=20,verbose_name="BP")
    tel = models.CharField(max_length=20, null=True, verbose_name="Téléphone ",
    validators= [RegexValidator(regex="^6[5-9]([0-9]){7}$",
    message="Entre un numéro valide")
    ])
    fax = models.CharField(max_length=90, null=True, verbose_name="Fax ")
    siteweb = models.CharField(max_length=30, null=True,verbose_name="Site web ")
    datecreationetab = models.CharField(max_length=90, null=True, verbose_name="Date création établissement")
    datetransformetab = models.CharField(max_length=30, null=True ,verbose_name="Date transformation établissement ",blank=True) 
    libellerelevenotelng1 = models.TextField(null=True, verbose_name="Libellé relevé de note langue1 ",blank=True)
    libellerelevenotelng2 = models.TextField(null=True, verbose_name="Libellé relevé de note langue2 ",blank=True)
    libelleattestationlng1 = models.TextField(null=True,verbose_name="Libellé attestation langue1 ",blank=True)
    libelleattestationlng2 = models.TextField(null=True, verbose_name="Libellé attestation langue2",blank=True)
    mentionbaspagerelevelng1 = models.TextField(null=True ,verbose_name="Mention bas page relevé langue1",blank=True) 
    mentionbaspagerelevelng2 = models.TextField(null=True, verbose_name="Mention bas page relevé langue2 ",blank=True)
    mentionbaspageattestlng1 = models.TextField(null=True, verbose_name="Mention bas page attestation langue1 ",blank=True)
    mentionbaspageattestlng2 = models.TextField(null=True, verbose_name="Mention bas page attestation langue2 ",blank=True)
    titrechefetablng1 = models.CharField(max_length=120,null=True,verbose_name="Titre chef établissement langue1",blank=True)
    titrechefetablng2 = models.CharField(max_length=120,null=True,verbose_name="Titre chef établissement langue2",blank=True)
    chainedroitecertiflng1 = models.TextField(null=True,verbose_name="Chaine drote certificat langue1",blank=True)
    chainedroitecertiflng2 = models.TextField(null=True ,verbose_name="Chaine drote certificat langue2",blank=True)
    libelleservicefinancier = models.CharField(max_length=120,null=True,verbose_name="Libellé service financier",blank=True)
    titredisciplinaire = models.TextField(null=True, verbose_name="Titre disciplinaire",blank=True)
    libelledisciplinaire = models.TextField(null=True, verbose_name="Libellé disciplinaire",blank=True)
    sanctiondisciplinaire = models.TextField(null=True, verbose_name="Sanction disciplinaire",blank=True)
    smtp_server = models.CharField(max_length=120,null=True ,verbose_name="Serveur SMTP",blank=True)
    login_mail = models.CharField(max_length=120,null=True,verbose_name="Login mail",blank=True)
    password_mail = models.CharField(max_length=120,null=True,verbose_name="Password mail",blank=True)
    courriel_mail = models.CharField(max_length=120,null=True,verbose_name="Courriel mail",blank=True)
    param_site = models.TextField(null=True, verbose_name="Paramettrage du site",blank=True)
    libellecertifscolaritelng1 = models.CharField(max_length=255,null=True,verbose_name="Libellé certificat de scolarité langue1",blank=True)
    libellecertifscolaritelng2 = models.CharField(max_length=255,null=True,verbose_name="Libellé certificat de scolarité langue2",blank=True)
    chainesignattestation = models.TextField(null=True,blank=True)
    chainesigcarteeleve = models.TextField(null=True,blank=True)
    chainesigrelevenote = models.TextField(null=True ,blank=True) 
    chainesigndiscipline = models.TextField(null=True,blank=True)
    mentionbaspagecertifscollng1 = models.TextField(null=True, verbose_name="Mention bas page certificat de scolarité langue1 ",blank=True)
    mentionbaspagecertifscollng2 = models.TextField(null=True, verbose_name="Mention bas page certificat de scolarité langue2 ",blank=True)
    
    def __str__(self):
        return self.libelleetablng1

class Ancien_etablissement(models.Model):
   
    codeancienetabli = models.CharField(max_length=30, verbose_name="Code ancien établissement", null=True,blank=True)
    libelleacetablng1 = models.CharField(max_length=30, verbose_name="Libellé ancien établissement langue1 ", null=True,blank=True)
    libelleacetablng2  = models.CharField(max_length=30, verbose_name="Libellé ancien établissement langue2", null=True,blank=True)

    def __str__(self):
        return self.libelleacetablng1

class Animateur_pedagogique(models.Model):
    
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE,verbose_name="Enseignant ")   
    anneescolaire = models.ForeignKey(Anneescolaire, on_delete=models.CASCADE,verbose_name="Année scolaire ")   
    discipline_competence = models.ForeignKey(Discipline_competence, on_delete=models.CASCADE,verbose_name="Discipline compétence")   
    codeanimateur = models.CharField(max_length=30, verbose_name="Code animateur", null=True,blank=True)
    dateselection = models.CharField(max_length=30, verbose_name="Date sélection", null=True,blank=True)

class Enseignant_titulaire(models.Model):
    
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE,verbose_name="Enseignant*")   
    anneescolaire = models.ForeignKey(Anneescolaire, on_delete=models.CASCADE,verbose_name="Année scolaire*")   
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE,verbose_name="Classe*")   
    codeeenseignanttitulaire = models.CharField(max_length=30, verbose_name="Code enseignant titulaire", null=True,blank=True)
    dateaffectation = models.CharField(max_length=30, verbose_name="Date affectation*", null=True)
    def __str__(self):
        return ' %s' % (self.enseignant)

class Typefrais(models.Model): 
    
    codetypefrais = models.CharField(max_length=30, verbose_name="Code type frais", null=True,blank=True)
    libelletypefraislng1 = models.CharField(max_length=130, verbose_name="Libellé type frais1", null=True)
    libelletypefraislng2 = models.CharField(max_length=130, verbose_name="Libellé type frais2", null=True,blank=True)
    def __str__(self):
        return self.libelletypefraislng1

class Fraispayer(models.Model):
    
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE,verbose_name="Série ")   
    anneescolaire = models.ForeignKey(Anneescolaire, on_delete=models.CASCADE,verbose_name="Année scolaire ")   
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE,verbose_name="Niveau")   
    typefrais = models.ForeignKey(Typefrais,on_delete=models.CASCADE, verbose_name="Type frais")
    codefraispayer = models.CharField(max_length=30, verbose_name="Code frais payer", null=True,blank=True)
    montant = models.IntegerField(verbose_name="Montant", null=True)

class Service(models.Model):
    etablissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE,verbose_name="Etablissement", blank=True)   
    codeservice = models.CharField(max_length=30,verbose_name="Code service")
    libelleservice = models.CharField(max_length=30,verbose_name="Libellé service")
    def __str__(self):
        return self.libelleservice

civ=(("M.","Mr."),("Mme.","Mme."),("Mlle.","Mlle."))
sexe=(("M","Masculin"),("F","Feminin"))
class Personnel(Personne):
    service = models.ForeignKey(Service, on_delete=models.CASCADE,verbose_name="Service*")
    etablissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE,verbose_name="Etablissement*")   
    #utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE,verbose_name="Utilisateur")   
    codepersonnel = models.CharField(max_length=30, null=True, verbose_name="Code personnel", blank=True)
    civilite = models.CharField(max_length=30, null=True, verbose_name="Civilité*",choices=civ)
    matriculepers = models.CharField(max_length=255, verbose_name="Matricule personnel", unique=True ,null=True, blank=True)
    numcni = models.CharField(max_length=255, verbose_name="Num CNI*")
    datedelivcni = models.CharField(max_length=90, verbose_name="Date de livraison CNI",null=True, blank=True)
    lieudelivcni = models.CharField(max_length=120, verbose_name="Lieu de livraison CNI", blank=True)
    persdelivcni = models.CharField(max_length=120, null=True, verbose_name="Personne de livraison CNI", blank=True)
    villageorigine = models.CharField(max_length=120, verbose_name="Village d'origine*",null=True)
    profession = models.CharField(max_length=120,  verbose_name="Profession*")
    nbreenfant = models.IntegerField(verbose_name="Nombres d'enfants")
    nomsenfants = models.TextField( verbose_name="Noms des enfants", blank=True)
    nomination = models.CharField(max_length=120,verbose_name="Nomination",null=True, blank=True)
    diplomesprof = models.CharField(max_length=130, verbose_name="Diplome professionnel",null=True, blank=True)
    lieudenaiss = models.CharField(max_length=30, verbose_name="Lieu de naissance*")
    sexe = models.CharField(max_length=20,choices=sexe,verbose_name="Sexe*")
    fonctionscivil = models.CharField(max_length=255, verbose_name="Fonction civil",null=True, blank=True)
    dateentreefctpub = models.CharField(max_length=90, verbose_name="Date d'entrée en fonction publique",null=True, blank=True)
    telephoneconj = models.CharField(max_length=9, verbose_name="Tel conjoint ",null=True, blank=True,
    validators= [RegexValidator(regex="^6[5-9]([0-9]){7}$",
    message="Entre un numéro de téléphone valide")
    ])   
    nomconj = models.CharField(max_length=120, verbose_name="Nom conjoint",null=True, blank=True)
    BP = models.CharField(max_length=120, verbose_name="BP",null=True, blank=True)
    fax = models.CharField(max_length=120,  verbose_name="Fax",null=True, blank=True)
    diplomeacad = models.CharField(max_length=120, verbose_name="Diplome academique*",null=True, blank=True)
    
    def __str__(self):
        return '%s %s' % (self.nom, self.prenom)

class Zone(models.Model):

    libelle = models.CharField(max_length=130,verbose_name="Libellé")
    description = models.CharField(max_length=130,verbose_name="Description",null=True, blank=True)
    def __str__(self):
        return self.libelle

class Bus(models.Model):

    matricule = models.CharField(max_length=130,verbose_name="Matricule")
    numero = models.CharField(max_length=130,verbose_name="Numéro")
    def __str__(self):
        return self.matricule
class Programme_trans(models.Model):
    
    personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE,verbose_name="Personnel ")   
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE,verbose_name="Zone ")   
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE,verbose_name="Bus")   
    heurdepart = models.CharField(max_length=30,verbose_name="Heur de départ", null=True,blank=True)
    date = models.CharField(max_length=30, verbose_name="Date", null=True,blank=True)



class Compteutilisateur(AbstractUser):
    photo = models.ImageField(validators=[validate_file_extension],verbose_name="Image ",blank=True)
    def __str__(self):
        return self.username 

class Elevecon(models.Model):
    ancien_etablissement = models.ForeignKey(Ancien_etablissement, on_delete=models.CASCADE,verbose_name="Ancien établissement*  ")   
    parents = models.ForeignKey(Parents, on_delete=models.CASCADE,verbose_name="Parent*  ")   
    codeeleveconc = models.CharField(max_length=30, verbose_name="Code de l'élève",blank=True)
    matriculeelevec = models.CharField(max_length=30 , verbose_name="Matricule*",unique=True)
    nomeelevec = models.CharField(max_length=30, verbose_name="Nom* ")
    prenomelevec = models.CharField(max_length=60, null=True, verbose_name="Prenom*")
    datenaisselevec = models.CharField(max_length=20,verbose_name="Date de naissance*")
    lieunaisselevec = models.CharField(max_length=30, null=True,verbose_name="Lieu de naissance*")
    sexe = models.CharField(max_length=20,choices=sexe,verbose_name="Sexe*")
    civilite = models.CharField(max_length=30, null=True, verbose_name="Civilité*",choices=civ)
    photo = models.FileField(validators=[validate_file_extension],verbose_name="Image ",blank=True)
    nationalite = models.CharField(max_length=30, null=True, verbose_name="Nationalité*")
    handicape = models.CharField(max_length=30, null=True,choices=handicap ,verbose_name="Handicape* ")
    langueofficielle = models.CharField(max_length=90, null=True, verbose_name="Langue officielle* ")
    emailelevec = models.CharField(max_length=50, verbose_name="Email ", blank=True)
    teleelevec = models.CharField(max_length=9, null=True, blank=True, verbose_name="Téléphone ",
    validators= [RegexValidator(regex="^6[5-9]([0-9]){7}$",
    message="Entre un numéro valide")
    ])
    villeresidence = models.CharField(max_length=30, null=True ,verbose_name="ville ",blank=True) 
    adresseel = models.CharField(max_length=90, null=True, verbose_name="Adresse* ")
    modeadmission = models.CharField(max_length=90, null=True, verbose_name="Mode d'admission* ")
    
    def __str__(self):
        return '%s %s' % (self.nomeelevec, self.prenomelevec)
class Eleverecruter(models.Model):
    anneescolaire = models.ForeignKey(Anneescolaire, on_delete=models.CASCADE,verbose_name="Année scolaire* ")   
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE,verbose_name="Niveau*")   
    elevecon = models.ForeignKey(Elevecon, on_delete=models.CASCADE,verbose_name="Elève*")   
    codeeleverecruter = models.CharField(max_length=30, verbose_name="Code élève recruté", null=True,blank=True)
    accepter = models.SmallIntegerField(verbose_name="Accepter",default=0)
    datederecrute = models.CharField(max_length=30, verbose_name="Date de recrutement*")
    dateConfirmerecrute = models.CharField(max_length=30, verbose_name="Date de la confirmation du recrutement*")
    def __str__(self):
        return ' %s' % (self.elevecon)

class Concours(models.Model):
    anneescolaire = models.ForeignKey(Anneescolaire, on_delete=models.CASCADE,verbose_name="Année scolaire* ")   
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE,verbose_name="Niveau*")   
    codeconcours = models.CharField(max_length=30,verbose_name="Code concours", null=True,blank=True)
    libelleconcours = models.CharField(max_length=30, verbose_name="Libellé concours*")
    codecentrecon = models.CharField(max_length=30, verbose_name="Code centre", null=True)
    session = models.CharField(max_length=30, verbose_name="Session*", null=True,blank=True)
    montant = models.IntegerField(verbose_name="Montant*",default=0)
    nbreplacesdisp = models.IntegerField(verbose_name="Nombres de place disponibles*")
    nbreplaceattente = models.IntegerField(verbose_name="Nombres de place en attente*")
    datedebutcon = models.CharField(max_length=30, verbose_name="Date début*")
    datefincon = models.CharField(max_length=30, verbose_name="Date fin*")

    def __str__(self):
        return self.libelleconcours

class InscriptionCon(models.Model):
    concours = models.ForeignKey(Concours, on_delete=models.CASCADE,verbose_name="Concours* ")   
    elevecon = models.ForeignKey(Elevecon, on_delete=models.CASCADE,verbose_name="Elève*")   
    codeinscripcon = models.CharField(max_length=30,verbose_name="Code inscription", null=True,blank=True)
    inscrit = models.SmallIntegerField(verbose_name="Inscrit*",default=0)
    dateinscription = models.CharField(max_length=30, verbose_name="Date inscription*")
    dateinscriptionConfirme = models.CharField(max_length=30, verbose_name="Date confirmation", null=True)

class Matiereconcours(models.Model):
    codematierecon = models.CharField(max_length=30,verbose_name="Code matière", null=True,blank=True)
    libellematcon = models.CharField(max_length=30, verbose_name="Libellé*")
    noteeliminatoire = models.FloatField(verbose_name="Note éliminatoire*",default=0.00000 )
    coefficientmatcon = models.IntegerField(verbose_name="Coefficient*",default=0)
    notemax = models.FloatField(verbose_name="Note max*",default=20.00000)

    def __str__(self):
        return self.libellematcon

class Certificatsco(models.Model):
    etablissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE,verbose_name="Etablissement* ")   
    anneescolaire = models.ForeignKey(Anneescolaire, on_delete=models.CASCADE,verbose_name="Année scolaire*")   
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE,verbose_name="Elève*")   
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE,verbose_name="Classe*")   
    codecertificat = models.CharField(max_length=30,verbose_name="Code certificat", null=True,blank=True)

    def __str__(self):
        return self.codecertificat

class Conseildiscipline(models.Model):
    sequence = models.ForeignKey(Sequence, on_delete=models.CASCADE,verbose_name="Séquence* ")   
    codeconseildiscipline = models.CharField(max_length=30,verbose_name="Code Conseil", null=True,blank=True)
    libelleconseildisc = models.CharField(max_length=100,verbose_name="Libellé conseil*", null=True,blank=True)
    dateconseil = models.CharField(max_length=100,verbose_name="Date de la tenue*", null=True,blank=True)
    libelledecision = models.CharField(max_length=230,verbose_name="Libellé décision*")
    membreconseil = models.CharField(max_length=230,verbose_name="Membre(s) du conseil*")

    def __str__(self):
        return self.libelleconseildisc

class Decisionconseil(models.Model):
    codedecision = models.CharField(max_length=30,verbose_name="Code décision", null=True,blank=True)
    libelledecision = models.CharField(max_length=100,verbose_name="Libellé décision*")

    def __str__(self):
        return self.libelledecision

class Decisionfinalconseil(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE,verbose_name="Nom complet élève* ")   
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE,verbose_name="Classe* ")   
    conseildiscipline = models.ForeignKey(Conseildiscipline, on_delete=models.CASCADE,verbose_name="Conseil discipline* ")   
    codedecisionfinalconseil = models.CharField(max_length=30,verbose_name="Code décision final conseil", null=True,blank=True)
    libelledecisionfinalconseil = models.CharField(max_length=100,verbose_name="Libellé décision final conseil*", null=True)

    def __str__(self):
        return self.libelledecisionfinalconseil



#test crypist

# class Registration(models.Model):
#     """
#     Modèle de l'inscription
#     """
#     CIVILITY_CHOICES = (
#         ('M.', 'M.'),
#         ('MME', 'Mme')
#     )
#     STREET_TYPE_CHOICES = (
#         ('Boulevard', 'Boulevard'),
#         ('Avenue', 'Avenue'),
#         ('Cours', 'Cours'),
#         ('Place', 'Place'),
#         ('Rue', 'Rue'),
#         ('Route', 'Route'),
#         ('Voie', 'Voie'),
#         ('Chemin', 'Chemin'),
#         ('Square', 'Square'),
#         ('Impasse', 'Impasse'),
#         ('Rond-point', 'Rond-point'),
#         ('Quai', 'Quai')
#     )

#     civility = models.CharField(max_length=3, choices=CIVILITY_CHOICES,
#                                 default='M.', verbose_name="Civilité")
#     birth_name = models.CharField(max_length=255, verbose_name="Nom de naissance")
#     last_name = models.CharField(max_length=255, blank=True, null=True,
#                                  verbose_name="Nom d'usage ou marital")
#     first_name = models.CharField(max_length=255, verbose_name="Prénom")
#     birth_date = models.DateField(verbose_name="Date de naissance ")
#     birth_place = models.CharField(max_length=255, verbose_name="Ville de naissance")
#     birth_country =models.CharField(max_length=255, verbose_name="Pays de naissance")
#     mail = models.EmailField(max_length=255, verbose_name="Mail")
#     street_type = models.CharField(max_length=30, verbose_name="Type de rue",
#                                    choices=STREET_TYPE_CHOICES, default='Rue')
#     street_number = models.CharField(max_length=30, verbose_name="Numéro de rue")
#     street = models.CharField(max_length=30, verbose_name="Rue")
#     comp_1 = models.CharField(max_length=255, verbose_name="Complément 1",
#                               blank=True, null=True)
#     comp_2 = models.CharField(max_length=255, verbose_name="Complément 2",
#                               blank=True, null=True)
#     city = models.CharField(max_length=255, verbose_name="Ville")
#     zip_code = models.CharField(max_length=255, verbose_name="Code postal")
#     country = models.CharField(max_length=255, verbose_name="Pays")
#     phone = models.CharField(max_length=255, blank=True, null=True,
#                              verbose_name="Téléphone")
#     comments = models.TextField(blank=True, null=True, verbose_name="Commentaires")
