# Generated by Django 2.2.9 on 2020-02-06 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mentorski', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upisi',
            name='predmet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentorski.Predmeti'),
        ),
        migrations.AlterField(
            model_name='upisi',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
