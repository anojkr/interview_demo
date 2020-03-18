# Generated by Django 3.0.4 on 2020-03-18 17:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_id', models.CharField(max_length=200, unique=True, verbose_name='Enrollment ID')),
                ('name', models.CharField(max_length=100, verbose_name='Student Name')),
                ('doj', models.DateField(verbose_name='D.O.J')),
                ('ranking', models.IntegerField(verbose_name='Ranking in school')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.CharField(max_length=200, unique=True, verbose_name='Employee ID')),
                ('name', models.CharField(max_length=200, verbose_name='Teacher Name')),
                ('doj', models.DateField(verbose_name='D.O.J')),
                ('salary', models.IntegerField(verbose_name='Salary')),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=200, verbose_name='Subject')),
                ('chapters', models.IntegerField(verbose_name='Chapters')),
                ('total_duration', models.IntegerField(verbose_name='Subject Duration')),
                ('class_duration', models.IntegerField(default=30, validators=[django.core.validators.MaxValueValidator(120), django.core.validators.MinValueValidator(30)], verbose_name='Class Duration')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms_apis.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Relative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relative_name', models.CharField(max_length=100, verbose_name='Relative Name')),
                ('relation', models.CharField(max_length=100, verbose_name='Relation ')),
                ('enrollment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms_apis.Student')),
            ],
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.CharField(max_length=50, verbose_name='Room No.')),
                ('seating_capacity', models.IntegerField(verbose_name='Seating Capacity')),
                ('web_support', models.BooleanField(verbose_name='Web Support')),
                ('shape', models.CharField(choices=[('oval', 'oval'), ('rectangular', 'rectangular'), ('canopy', 'canopy'), ('elevated', 'elevated')], default='rectangular', max_length=50, verbose_name='Class Shape')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms_apis.Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms_apis.Subjects')),
            ],
        ),
    ]
