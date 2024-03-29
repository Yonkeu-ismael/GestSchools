# Generated by Django 2.2.2 on 2019-06-23 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestschools', '0002_auto_20190623_1255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emploi_temps',
            name='codecoursdispenser',
        ),
        migrations.RemoveField(
            model_name='emploi_temps',
            name='jours',
        ),
        migrations.AlterField(
            model_name='emploi_temps',
            name='matiere',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestschools.Matiere', verbose_name='Matière'),
        ),
        migrations.CreateModel(
            name='CoursMardi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classe', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='gestschools.Classe', verbose_name='Classe')),
                ('matiere', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='gestschools.Matiere', verbose_name='Matière')),
            ],
        ),
        migrations.AddField(
            model_name='emploi_temps',
            name='coursmardi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestschools.CoursMardi', verbose_name='Cours Mardi'),
        ),
    ]
