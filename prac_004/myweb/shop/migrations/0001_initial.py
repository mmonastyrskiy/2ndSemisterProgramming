# Generated by Django 4.0.3 on 2022-04-30 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('self_id', models.IntegerField()),
                ('Brand_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_parent', models.IntegerField()),
                ('self_id', models.IntegerField()),
                ('name', models.CharField(max_length=1000)),
                ('text_html', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('self_id', models.IntegerField()),
                ('arts', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('link', models.CharField(max_length=1000)),
                ('description', models.TextField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.catalog')),
            ],
        ),
    ]