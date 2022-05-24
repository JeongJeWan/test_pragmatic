# Generated by Django 3.2.12 on 2022-05-24 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mapapp', '0003_remove_map_project'),
        ('commentapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='article',
        ),
        migrations.AddField(
            model_name='comment',
            name='map',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment', to='mapapp.map'),
        ),
    ]
