# Generated by Django 3.1.7 on 2021-04-02 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        ('articles', '0002_auto_20210401_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='article', to='projects.project'),
        ),
    ]
