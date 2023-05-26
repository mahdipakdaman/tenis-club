# Generated by Django 4.0.5 on 2023-05-26 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_member_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=255)),
                ('inventory', models.IntegerField()),
                ('productpic', models.ImageField(upload_to='photos/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]