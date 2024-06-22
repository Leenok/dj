# Generated by Django 5.0.6 on 2024-06-16 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_pzzle_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producer_name', models.CharField(max_length=100)),
                ('producer_country', models.CharField(max_length=100)),
                ('producer_leval', models.IntegerField()),
                ('producer_img', models.ImageField(blank=True, upload_to='app1/static/img/producer')),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style_name', models.CharField(max_length=30)),
            ],
        ),
    ]