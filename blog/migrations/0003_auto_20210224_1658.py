# Generated by Django 3.1.7 on 2021-02-24 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210224_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='lastname_student',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
