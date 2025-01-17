# Generated by Django 5.0.3 on 2024-03-28 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0005_delete_crud'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('grade', models.CharField(max_length=6)),
                ('address', models.TextField()),
                ('contact_number', models.CharField(max_length=20)),
            ],
        ),
    ]
