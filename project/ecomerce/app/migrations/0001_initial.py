# Generated by Django 5.0.6 on 2024-05-11 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=150)),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField(max_length=150)),
            ],
        ),
    ]
