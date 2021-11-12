# Generated by Django 3.2.7 on 2021-11-12 03:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventarioApp', '0009_auto_20211111_1340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='email',
        ),
        migrations.RemoveField(
            model_name='proveedor',
            name='email',
        ),
        migrations.AddField(
            model_name='cliente',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='calificacion',
            field=models.IntegerField(choices=[(1, '★'), (2, '★ ★'), (3, '★ ★ ★'), (4, '★ ★ ★ ★'), (5, '★ ★ ★ ★ ★')], default=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventarioApp.proveedor'),
        ),
    ]
