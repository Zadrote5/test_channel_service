# Generated by Django 4.0.4 on 2022-05-19 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheet_id', models.CharField(max_length=30)),
                ('price_dollars', models.IntegerField()),
                ('price_rub', models.IntegerField()),
                ('delivery_date', models.DateField()),
            ],
        ),
    ]
