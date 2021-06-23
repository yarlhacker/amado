# Generated by Django 3.2.4 on 2021-06-21 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now=True)),
                ('status', models.BooleanField()),
                ('description_newsletter', models.TextField()),
                ('copyrigths', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Configuration',
                'verbose_name_plural': 'Configurations',
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now=True)),
                ('status', models.BooleanField()),
                ('email', models.EmailField(max_length=250)),
            ],
            options={
                'verbose_name': 'Newsletter',
                'verbose_name_plural': 'Newsletters',
            },
        ),
        migrations.CreateModel(
            name='Sociaux',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now=True)),
                ('status', models.BooleanField()),
                ('url', models.URLField(max_length=250)),
                ('nom', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Social',
                'verbose_name_plural': 'Sociaux',
            },
        ),
        migrations.CreateModel(
            name='website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now=True)),
                ('status', models.BooleanField()),
                ('nom_site', models.CharField(max_length=250)),
                ('logo_site', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'website',
                'verbose_name_plural': 'websites',
            },
        ),
    ]
