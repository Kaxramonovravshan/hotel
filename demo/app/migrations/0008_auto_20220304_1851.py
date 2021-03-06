# Generated by Django 3.2.8 on 2022-03-04 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20220216_2046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='User name')),
                ('number', models.IntegerField(blank=True, default=0, verbose_name='Phone number')),
            ],
            options={
                'verbose_name': 'Name',
                'verbose_name_plural': 'Name',
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.RemoveField(
            model_name='productcolor',
            name='color',
        ),
        migrations.RemoveField(
            model_name='productcolor',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productcolorsize',
            name='memory',
        ),
        migrations.RemoveField(
            model_name='productcolorsize',
            name='productColor',
        ),
        migrations.RemoveField(
            model_name='productgallery',
            name='productColor',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Color',
        ),
        migrations.DeleteModel(
            name='Memory',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductColor',
        ),
        migrations.DeleteModel(
            name='ProductColorSize',
        ),
        migrations.DeleteModel(
            name='ProductGallery',
        ),
    ]
