# Generated by Django 2.1.7 on 2019-04-08 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_enrollment_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group_Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Group')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Test')),
            ],
        ),
    ]