# Generated by Django 3.1.7 on 2021-03-14 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_organization_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='contact_name',
            field=models.CharField(default='Jane Doe', max_length=125),
            preserve_default=False,
        ),
    ]
