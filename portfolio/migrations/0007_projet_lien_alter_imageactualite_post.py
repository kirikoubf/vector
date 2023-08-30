# Generated by Django 4.1.4 on 2023-08-30 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_actualite_parto'),
    ]

    operations = [
        migrations.AddField(
            model_name='projet',
            name='lien',
            field=models.TextField(default='/'),
        ),
        migrations.AlterField(
            model_name='imageactualite',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='portfolio.actualite'),
        ),
    ]
