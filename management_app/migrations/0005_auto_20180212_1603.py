# Generated by Django 2.1 on 2018-02-12 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management_app', '0004_auto_20180212_0443'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_app.Field')),
            ],
        ),
        migrations.AddField(
            model_name='school',
            name='rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=70, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='student',
            name='program',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='management_app.Program'),
        ),
    ]
