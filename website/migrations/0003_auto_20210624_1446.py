# Generated by Django 3.2.4 on 2021-06-24 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_website_logo_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='sociaux',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='website',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]