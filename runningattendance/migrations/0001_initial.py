# Generated by Django 2.2.3 on 2020-03-02 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('infosys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Takeleave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('reason', models.CharField(max_length=50)),
                ('inspector', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='takeleave_inspector', to='infosys.Student')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infosys.Student')),
            ],
            options={
                'verbose_name': '请假',
                'verbose_name_plural': '请假',
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('inspector', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attendance_inspector', to='infosys.Student')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infosys.Student')),
            ],
            options={
                'verbose_name': '考勤',
                'verbose_name_plural': '考勤',
            },
        ),
    ]