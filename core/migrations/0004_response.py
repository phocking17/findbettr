# Generated by Django 3.1.7 on 2021-03-14 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_tag_type_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overall_tags_selected', models.ManyToManyField(to='core.Arching_Tag')),
                ('tags_completed', models.ManyToManyField(to='core.Tag_Type')),
                ('tags_selected', models.ManyToManyField(to='core.Tag')),
            ],
        ),
    ]
