# Generated by Django 3.1 on 2020-08-24 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200824_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodata',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]