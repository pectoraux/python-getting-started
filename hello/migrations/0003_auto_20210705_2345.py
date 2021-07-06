# Generated by Django 2.2.12 on 2021-07-05 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20210705_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='description',
        ),
        migrations.RemoveField(
            model_name='document',
            name='document',
        ),
        migrations.AddField(
            model_name='document',
            name='document_id',
            field=models.FileField(default=1, upload_to='static/', verbose_name='Proof of identity'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='document_utility',
            field=models.FileField(default=1, upload_to='static/', verbose_name='Proof of residence'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
