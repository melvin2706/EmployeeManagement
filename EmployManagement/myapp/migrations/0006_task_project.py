# Generated by Django 4.0.4 on 2023-05-04 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.project'),
        ),
    ]
