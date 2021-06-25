# Generated by Django 3.2.4 on 2021-06-24 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20210624_1446'),
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('prix', models.CharField(max_length=255)),
                ('quantite', models.CharField(max_length=255)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_payement', to='service.article')),
                ('checkout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkout_payement', to='checkout.checkout')),
            ],
            options={
                'verbose_name': 'Payement',
                'verbose_name_plural': 'Payements',
            },
        ),
    ]