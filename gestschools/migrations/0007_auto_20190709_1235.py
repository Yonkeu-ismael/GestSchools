# Generated by Django 2.2.2 on 2019-07-09 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestschools', '0006_auto_20190627_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codejour', models.CharField(blank=True, max_length=20, null=True, verbose_name='Code jours')),
                ('libellejourlng1', models.CharField(max_length=20, null=True, verbose_name='Libellé jours1')),
                ('libellejourlng2', models.CharField(blank=True, max_length=20, null=True, verbose_name='Libellé jours2')),
            ],
        ),
        migrations.RemoveField(
            model_name='moyennesequentiel',
            name='codemoyenneseq',
        ),
        migrations.AlterField(
            model_name='absence',
            name='codeeabcence',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Code absence'),
        ),
        migrations.AlterField(
            model_name='evaluernote',
            name='note',
            field=models.FloatField(default=0.0, null=True, verbose_name='Note'),
        ),
        migrations.AlterField(
            model_name='moyennesequentiel',
            name='absence',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Absence'),
        ),
        migrations.AlterField(
            model_name='moyennesequentiel',
            name='appreciationconduite',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Appréciation conduite'),
        ),
        migrations.AlterField(
            model_name='moyennesequentiel',
            name='appreciationtravail',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Appréciation du travail'),
        ),
        migrations.AlterField(
            model_name='moyennesequentiel',
            name='avertissementconduite',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Avertissement conduite'),
        ),
        migrations.AlterField(
            model_name='moyennesequentiel',
            name='avertissementtravail',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Avertissement travail'),
        ),
        migrations.AlterField(
            model_name='moyennesequentiel',
            name='blameconduite',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Blame conduite'),
        ),
        migrations.AlterField(
            model_name='moyennesequentiel',
            name='blametravail',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Blame travail'),
        ),
        migrations.AlterField(
            model_name='moyennesequentiel',
            name='decisionseq',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Décision séquence'),
        ),
        migrations.AlterField(
            model_name='moyennesequentiel',
            name='encouragements',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Encouragements'),
        ),
        migrations.AlterField(
            model_name='moyennesequentiel',
            name='exclusions',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Exclusions'),
        ),
        migrations.AlterField(
            model_name='moyennesequentiel',
            name='felicitation',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Félicitation'),
        ),
        migrations.AlterField(
            model_name='moyennesequentiel',
            name='listematieremauvais',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Liste matière mauvaise'),
        ),
        migrations.AlterField(
            model_name='moyennesequentiel',
            name='tableauhonneur',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name="Tableau d'honneur"),
        ),
        migrations.CreateModel(
            name='Programmation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeprogrammation', models.CharField(blank=True, max_length=20, null=True, verbose_name='Code programmation')),
                ('affectation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestschools.Affectation', verbose_name='Affectation')),
                ('classe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestschools.Classe', verbose_name='Classe')),
                ('jours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestschools.Jours', verbose_name='Jours')),
                ('plage_horaire', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestschools.Plage_horaire', verbose_name='Plage horaire')),
            ],
        ),
    ]