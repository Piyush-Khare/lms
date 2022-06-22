# Generated by Django 4.0.5 on 2022-06-22 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_books_delete_flag_alter_books_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='status',
            field=models.CharField(choices=[('Available', 'Available'), ('Not Available', 'Not Available')], default='Available', max_length=50),
        ),
    ]
