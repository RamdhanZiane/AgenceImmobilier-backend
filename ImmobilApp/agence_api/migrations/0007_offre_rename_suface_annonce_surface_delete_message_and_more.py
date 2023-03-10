# Generated by Django 4.1.4 on 2022-12-28 20:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agence_api', '0006_alter_annonce_insertdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=1000)),
                ('prix', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='annonce',
            old_name='suface',
            new_name='surface',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.AddField(
            model_name='offre',
            name='annonce',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agence_api.annonce'),
        ),
        migrations.AddField(
            model_name='offre',
            name='annonceur',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='annonceurs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='offre',
            name='client',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='clients', to=settings.AUTH_USER_MODEL),
        ),
    ]
