# Generated by Django 4.2.13 on 2024-06-12 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('TECH', 'Technology'), ('LIFE', 'Lifestyle'), ('FIN', 'Finance'), ('EDU', 'Education'), ('ENT', 'Entertainment'), ('OTR', 'Other')], default='OTR', max_length=4),
        ),
        migrations.AlterField(
            model_name='post',
            name='banner',
            field=models.ImageField(blank=True, default='../static/assets/fallback.webp', upload_to=''),
        ),
    ]