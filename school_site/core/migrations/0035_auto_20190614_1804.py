# Generated by Django 2.2.2 on 2019-06-14 15:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_attachedfileachievement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachedfileachievement',
            name='student',
        ),
        migrations.AddField(
            model_name='achievement',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='attachedfileachievement',
            name='achievement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='achievement_files', to='core.Achievement'),
        ),
        migrations.AlterField(
            model_name='background',
            name='page',
            field=models.CharField(choices=[('home', 'home'), ('about', 'about'), ('gallery', 'gallery'), ('schedule', 'schedule'), ('students', 'students'), ('news', 'news'), ('achievements', 'achievements')], default='home', max_length=25),
        ),
    ]