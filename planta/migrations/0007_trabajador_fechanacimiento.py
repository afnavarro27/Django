# Generated by Django 4.0.6 on 2022-08-08 15:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('planta', '0006_alter_productos_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajador',
            name='fechaNacimiento',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]