# Generated by Django 4.1.2 on 2023-05-14 14:17

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_excelfileupload'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ExcelFileUpload',
        ),
        migrations.AlterField(
            model_name='student',
            name='Email',
            field=models.EmailField(error_messages={'required': 'Please provide your email address.', 'unique': 'An account with this email exist.'}, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Phone_no',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
    ]