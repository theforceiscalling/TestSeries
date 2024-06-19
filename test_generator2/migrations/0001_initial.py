# Generated by Django 5.0.4 on 2024-06-19 08:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('class_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_generator2.class')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_generator2.module')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(choices=[('theory', 'Theory'), ('mcq', 'MCQ'), ('assertion_reason', 'Assertion and Reason'), ('competency_case', 'Competency/Case Based')], default='theory', max_length=20)),
                ('question_text', models.TextField()),
                ('solution', models.TextField(blank=True, null=True)),
                ('max_marks', models.IntegerField(default=0)),
                ('pyq', models.CharField(max_length=20)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('added_by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_generator2.chapter')),
                ('class_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_generator2.class')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_generator2.module')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_generator2.subject')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_generator2.subject'),
        ),
    ]