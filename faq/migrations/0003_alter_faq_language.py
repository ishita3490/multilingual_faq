# Generated by Django 4.2.18 on 2025-02-02 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0002_faq_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('hi', 'Hindi'), ('bn', 'Bengali')], default='en', max_length=10),
        ),
    ]
