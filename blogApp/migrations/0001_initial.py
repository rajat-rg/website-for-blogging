# Generated by Django 3.1.6 on 2021-04-23 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('slug', models.CharField(max_length=130)),
                ('content', models.TextField(max_length=600)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]