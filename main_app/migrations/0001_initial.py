# Generated by Django 3.0.7 on 2020-06-29 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('start_quiz', models.DateTimeField()),
                ('end_quiz', models.DateTimeField()),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
