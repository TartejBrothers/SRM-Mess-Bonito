# Generated by Django 5.0.1 on 2024-02-26 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0004_alter_details_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Values',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('lunch', models.IntegerField()),
                ('dinner', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
        ),
    ]
