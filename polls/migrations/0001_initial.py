# Generated by Django 2.1.7 on 2019-04-08 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('objectives', models.CharField(max_length=200)),
                ('room', models.CharField(max_length=50)),
                ('day', models.CharField(max_length=10)),
                ('start_time', models.CharField(max_length=10)),
                ('end_time', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('choices', models.CharField(max_length=100)),
                ('difficulty', models.IntegerField(choices=[(1, 'easy'), (2, 'medium'), (3, 'hard')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('level', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='individual_Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(default='', max_length=50)),
                ('age', models.IntegerField()),
                ('code', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('experience', models.IntegerField(default=0)),
                ('specilization', models.CharField(choices=[('math', 'Math'), ('physics', 'Physics'), ('arts', 'Arts')], default='math', max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='individual_assignment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Student'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Teacher'),
        ),
    ]
