# Generated by Django 5.1.4 on 2025-01-13 18:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.AddField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='event',
            name='priority',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.category'),
        ),
    ]
