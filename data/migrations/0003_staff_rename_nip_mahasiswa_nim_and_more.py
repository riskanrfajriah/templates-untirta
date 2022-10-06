# Generated by Django 4.1 on 2022-10-06 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_mahasiswa'),
    ]

    operations = [
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('NIP', models.CharField(max_length=40)),
                ('tanggal_lahir', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('unit', models.CharField(max_length=40)),
                ('alamat', models.CharField(max_length=40)),
            ],
        ),
        migrations.RenameField(
            model_name='mahasiswa',
            old_name='NIP',
            new_name='NIM',
        ),
        migrations.RemoveField(
            model_name='mahasiswa',
            name='alamat',
        ),
    ]
