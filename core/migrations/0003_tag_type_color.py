# Generated by Django 3.1.7 on 2021-03-13 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_tag_type_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag_type',
            name='color',
            field=models.CharField(default='#000000', max_length=7),
            preserve_default=False,
        ),
    ]
