# Generated by Django 5.0.1 on 2024-02-01 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lunch', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=35)),
                ('dinner', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=35)),
            ],
        ),
    ]
