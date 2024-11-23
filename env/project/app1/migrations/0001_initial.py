# Generated by Django 5.1.3 on 2024-11-23 04:14

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
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('priority', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=20)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'completed')], max_length=20)),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]