# Generated by Django 2.2.2 on 2019-07-10 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestschools', '0009_auto_20190710_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeq', models.CharField(max_length=60, verbose_name='Code qualification')),
                ('libellequalif', models.CharField(max_length=60, verbose_name='Libellé')),
            ],
        ),
        migrations.AlterField(
            model_name='parents',
            name='emailtuteur',
            field=models.CharField(blank=True, max_length=90, null=True, verbose_name='Email tuteur'),
        ),
        migrations.AlterField(
            model_name='parents',
            name='nommere',
            field=models.CharField(max_length=30, verbose_name='Nom mère*'),
        ),
        migrations.AlterField(
            model_name='parents',
            name='nompere',
            field=models.CharField(max_length=60, verbose_name='Nom père*'),
        ),
        migrations.AlterField(
            model_name='parents',
            name='nomtuteur',
            field=models.CharField(blank=True, max_length=20, verbose_name='Nom tuteur'),
        ),
        migrations.AlterField(
            model_name='parents',
            name='professionpere',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Profession père'),
        ),
        migrations.AlterField(
            model_name='parents',
            name='telmere',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Tel mère'),
        ),
        migrations.AlterField(
            model_name='parents',
            name='telpere',
            field=models.CharField(max_length=30, null=True, verbose_name='Tel père*'),
        ),
        migrations.AlterField(
            model_name='parents',
            name='teltuteur',
            field=models.CharField(blank=True, max_length=90, verbose_name='Tel tuteur'),
        ),
        migrations.AlterField(
            model_name='parents',
            name='ville',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestschools.Ville', verbose_name='Ville*'),
        ),
        migrations.AddField(
            model_name='enseignant',
            name='qualification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestschools.Qualification', verbose_name='Qualification'),
        ),
    ]
