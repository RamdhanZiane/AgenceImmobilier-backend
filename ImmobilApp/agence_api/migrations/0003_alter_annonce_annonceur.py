# Generated by Django 4.1.4 on 2022-12-25 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agence_api', '0002_alter_annonce_annonceur_favoris'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='annonceur',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
