# Generated by Django 5.0.7 on 2024-07-14 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_scope_articlescope_article_articles'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlescope',
            old_name='topic',
            new_name='tag',
        ),
        migrations.RenameField(
            model_name='scope',
            old_name='topic',
            new_name='name',
        ),
    ]
