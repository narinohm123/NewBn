# Generated by Django 3.2.8 on 2021-10-29 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('Author', models.CharField(max_length=255)),
                ('faculty_doc', models.CharField(max_length=255, null=True)),
                ('date_request', models.DateField()),
                ('date_evaluate', models.DateField()),
                ('date_expire', models.DateField()),
                ('level_evaluate_tech', models.CharField(max_length=255)),
                ('level_evaluate_document', models.CharField(max_length=255)),
                ('no_evaluate', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='Author',
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_evaluate',
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_expire',
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_request',
        ),
        migrations.RemoveField(
            model_name='user',
            name='faculty_doc',
        ),
        migrations.RemoveField(
            model_name='user',
            name='level_evaluate_document',
        ),
        migrations.RemoveField(
            model_name='user',
            name='level_evaluate_tech',
        ),
        migrations.RemoveField(
            model_name='user',
            name='no_evaluate',
        ),
    ]
