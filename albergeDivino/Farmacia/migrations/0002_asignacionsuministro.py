# Generated by Django 5.0.6 on 2024-07-06 01:10

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmacia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsignacionSuministro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asignado_a', models.CharField(max_length=100)),
                ('fecha_asignacion', models.DateField(default=django.utils.timezone.now)),
                ('cantidad', models.PositiveIntegerField()),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmacia.medicamento')),
            ],
            options={
                'verbose_name': 'Asignación de Suministro',
                'verbose_name_plural': 'Asignaciones de Suministro',
                'ordering': ['-fecha_asignacion'],
            },
        ),
    ]
