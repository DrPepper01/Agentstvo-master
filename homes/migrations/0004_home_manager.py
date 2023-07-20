# Generated by Django 4.2.3 on 2023-07-20 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0001_initial'),
        ('homes', '0003_home_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='managers.manager'),
        ),
    ]
