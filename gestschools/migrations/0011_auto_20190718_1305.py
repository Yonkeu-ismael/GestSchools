# Generated by Django 2.2.2 on 2019-07-18 12:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestschools', '0010_auto_20190710_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrateur',
            name='date_naiss',
            field=models.DateField(verbose_name='Date de Naissance*'),
        ),
        migrations.AlterField(
            model_name='administrateur',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail*'),
        ),
        migrations.AlterField(
            model_name='administrateur',
            name='lieu_naiss',
            field=models.CharField(max_length=100, verbose_name='Lieu de naissance*'),
        ),
        migrations.AlterField(
            model_name='administrateur',
            name='nom',
            field=models.CharField(max_length=100, verbose_name='Nom*'),
        ),
        migrations.AlterField(
            model_name='administrateur',
            name='prenom',
            field=models.CharField(max_length=100, verbose_name='Prénom*'),
        ),
        migrations.AlterField(
            model_name='administrateur',
            name='telephone',
            field=models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(message='Entrer un numéro de telephone valide', regex='^6[5-9]([0-9]){7}$')], verbose_name='Téléphone*'),
        ),
        migrations.AlterField(
            model_name='arrondissement',
            name='codearrondissement',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Code arrondissement'),
        ),
        migrations.AlterField(
            model_name='arrondissement',
            name='departement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestschools.Departementgeo', verbose_name='Departement*'),
        ),
        migrations.AlterField(
            model_name='arrondissement',
            name='libellearronlng1',
            field=models.CharField(max_length=60, verbose_name='Libellé1*'),
        ),
        migrations.AlterField(
            model_name='arrondissement',
            name='libellearronlng2',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Libellé2'),
        ),
        migrations.AlterField(
            model_name='departementgeo',
            name='codedepartementgeo',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Code département'),
        ),
        migrations.AlterField(
            model_name='departementgeo',
            name='libelledelegationdeparlng1',
            field=models.CharField(max_length=60, verbose_name='Libellé délégation départemental1*'),
        ),
        migrations.AlterField(
            model_name='departementgeo',
            name='libelledelegationdeparlng2',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Libellé délégation départemental2'),
        ),
        migrations.AlterField(
            model_name='departementgeo',
            name='libelledepartlng1',
            field=models.CharField(max_length=60, verbose_name='Libellé département1*'),
        ),
        migrations.AlterField(
            model_name='departementgeo',
            name='libelledepartlng2',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Libellé département2'),
        ),
        migrations.AlterField(
            model_name='departementgeo',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestschools.Region', verbose_name='Region*'),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='adresseens',
            field=models.CharField(max_length=90, null=True, verbose_name='Adresse*'),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='civilite',
            field=models.CharField(choices=[('M.', 'Mr.'), ('Mme.', 'Mme.'), ('Mlle.', 'Mlle.')], max_length=30, null=True, verbose_name='Civilité*'),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='date_naiss',
            field=models.DateField(verbose_name='Date de Naissance*'),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='diplomeacademique',
            field=models.CharField(max_length=250, verbose_name='Diplome académique*'),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='discipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestschools.Discipline_competence', verbose_name='Discipline*'),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail*'),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='langueofficielle',
            field=models.CharField(max_length=90, null=True, verbose_name='Langue officielle*'),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='lieu_naiss',
            field=models.CharField(max_length=100, verbose_name='Lieu de naissance*'),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='nationalite',
            field=models.CharField(max_length=30, verbose_name='Nationalité*'),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='nom',
            field=models.CharField(max_length=100, verbose_name='Nom*'),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='prenom',
            field=models.CharField(max_length=100, verbose_name='Prénom*'),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='profession',
            field=models.CharField(max_length=90, verbose_name='Profession*'),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='qualification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestschools.Qualification', verbose_name='Qualification*'),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='regionorigine',
            field=models.CharField(max_length=50, null=True, verbose_name="Région d'origine*"),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='sexe',
            field=models.CharField(choices=[('M', 'Masculin'), ('F', 'Feminin')], max_length=20, verbose_name='Sexe*'),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='telephone',
            field=models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(message='Entrer un numéro de telephone valide', regex='^6[5-9]([0-9]){7}$')], verbose_name='Téléphone*'),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='villeresidence',
            field=models.CharField(max_length=90, null=True, verbose_name='Ville de residence*'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='civilite',
            field=models.CharField(choices=[('M.', 'Mr.'), ('Mme.', 'Mme.'), ('Mlle.', 'Mlle.')], max_length=30, null=True, verbose_name='Civilité*'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='date_naiss',
            field=models.DateField(verbose_name='Date de Naissance*'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='diplomeacad',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Diplome academique*'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail*'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='etablissement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestschools.Etablissement', verbose_name='Etablissement*'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='lieu_naiss',
            field=models.CharField(max_length=100, verbose_name='Lieu de naissance*'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='lieudenaiss',
            field=models.CharField(max_length=30, verbose_name='Lieu de naissance*'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='nom',
            field=models.CharField(max_length=100, verbose_name='Nom*'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='numcni',
            field=models.CharField(max_length=255, verbose_name='Num CNI*'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='prenom',
            field=models.CharField(max_length=100, verbose_name='Prénom*'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='profession',
            field=models.CharField(max_length=120, verbose_name='Profession*'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestschools.Service', verbose_name='Service*'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='sexe',
            field=models.CharField(choices=[('M', 'Masculin'), ('F', 'Feminin')], max_length=20, verbose_name='Sexe*'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='telephone',
            field=models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(message='Entrer un numéro de telephone valide', regex='^6[5-9]([0-9]){7}$')], verbose_name='Téléphone*'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='telephoneconj',
            field=models.CharField(blank=True, max_length=9, null=True, validators=[django.core.validators.RegexValidator(message='Entre un numéro de téléphone valide', regex='^6[5-9]([0-9]){7}$')], verbose_name='Tel conjoint '),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='villageorigine',
            field=models.CharField(max_length=120, null=True, verbose_name="Village d'origine*"),
        ),
        migrations.AlterField(
            model_name='ville',
            name='arrondissement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestschools.Arrondissement', verbose_name='Arrondissement*'),
        ),
        migrations.AlterField(
            model_name='ville',
            name='codeville',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Code ville'),
        ),
        migrations.AlterField(
            model_name='ville',
            name='libellevillelng1',
            field=models.CharField(max_length=60, verbose_name='Libellé1*'),
        ),
        migrations.AlterField(
            model_name='ville',
            name='libellevillelng2',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Libellé2'),
        ),
    ]