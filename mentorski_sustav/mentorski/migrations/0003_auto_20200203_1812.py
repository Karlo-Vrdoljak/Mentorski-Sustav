# Generated by Django 2.2.9 on 2020-02-03 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorski', '0002_predmeti_upisi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predmeti',
            name='izborni',
            field=models.CharField(choices=[('ne', 'ne'), ('da', 'da')], default='ne', max_length=2),
        ),
    ]
