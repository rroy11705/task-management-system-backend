# Generated by Django 5.0.1 on 2024-01-25 07:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=64, unique=True)),
                ('title', models.CharField(max_length=2045)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('child_of', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='tasks.task')),
                ('labels', models.ManyToManyField(related_name='labels', to='tasks.tasklabel')),
                ('status', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='tasks.taskstatus')),
            ],
        ),
    ]
