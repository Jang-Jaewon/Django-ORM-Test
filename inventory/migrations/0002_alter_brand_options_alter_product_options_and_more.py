# Generated by Django 4.0.6 on 2022-08-03 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name_plural': 'Brand'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Product'},
        ),
        migrations.AlterModelOptions(
            name='stock',
            options={'verbose_name_plural': 'Stock'},
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Brand Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='no-name', help_text='This is the help text', max_length=100, verbose_name='Product Name'),
        ),
    ]
