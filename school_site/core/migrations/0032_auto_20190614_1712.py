# Generated by Django 2.2.2 on 2019-06-14 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_auto_20190613_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttachedFileStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='attached_files')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('image', models.ImageField(blank=True, default=None, upload_to='student_pics')),
                ('content', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='AttachedFileStudentItem',
        ),
        migrations.DeleteModel(
            name='StudentItem',
        ),
        migrations.AddField(
            model_name='attachedfilestudent',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_files', to='core.Student'),
        ),
    ]