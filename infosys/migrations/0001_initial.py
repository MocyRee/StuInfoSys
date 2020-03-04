# Generated by Django 2.2.3 on 2020-03-02 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('class_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=30)),
                ('grade', models.CharField(max_length=4)),
                ('major', models.CharField(max_length=20)),
                ('college', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Class',
                'verbose_name_plural': 'Class',
            },
        ),
        migrations.CreateModel(
            name='Dormitory',
            fields=[
                ('dormitory_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('building_num', models.CharField(max_length=5, null=True)),
                ('room_num', models.CharField(max_length=4, null=True)),
                ('floor', models.CharField(max_length=2, null=True)),
            ],
            options={
                'verbose_name': 'Dormitory',
                'verbose_name_plural': 'Dormitory',
            },
        ),
        migrations.CreateModel(
            name='Live',
            fields=[
                ('live_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('bed_num', models.CharField(max_length=2, null=True)),
                ('dormitory_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='infosys.Dormitory')),
            ],
            options={
                'verbose_name': 'Live',
                'verbose_name_plural': 'Live',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=20)),
                ('student_sex', models.CharField(max_length=2)),
                ('student_birth', models.DateField(null=True)),
                ('student_address', models.CharField(max_length=100)),
                ('student_tel', models.CharField(max_length=20)),
                ('student_qq', models.CharField(max_length=20)),
                ('class_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='infosys.Class')),
                ('live_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='infosys.Live')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Student',
            },
        ),
        migrations.AddField(
            model_name='live',
            name='student_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='infosys.Student'),
        ),
        migrations.AddField(
            model_name='dormitory',
            name='master',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='infosys.Live'),
        ),
    ]