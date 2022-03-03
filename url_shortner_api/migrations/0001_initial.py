# Generated by Django 4.0.3 on 2022-03-03 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_link', models.URLField(max_length=1000)),
                ('shortened_link', models.URLField(blank=True, editable=False, null=True)),
            ],
        ),
    ]
