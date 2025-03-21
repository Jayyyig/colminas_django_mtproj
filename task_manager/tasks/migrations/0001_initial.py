# Generated by Django 5.1.7 on 2025-03-07 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=100, null=True)),
                ('due_date', models.DateField()),
                ('status', models.CharField(default='Pending', max_length=20)),
            ],
        ),
    ]
