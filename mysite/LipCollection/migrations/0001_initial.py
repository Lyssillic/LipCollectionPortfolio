# Generated by Django 2.2 on 2020-11-13 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LipItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Brand', models.CharField(max_length=200)),
                ('Flavor', models.CharField(max_length=200)),
                ('Category', models.CharField(max_length=200)),
                ('Picture', models.ImageField(default='lipItem.PNG', upload_to='media')),
                ('Price', models.IntegerField()),
                ('Rarity', models.CharField(max_length=200)),
            ],
        ),
    ]
