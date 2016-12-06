# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-05 10:58
from __future__ import unicode_literals

import App.models
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Question_1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': '1 Mark Questions',
                'verbose_name': '1 Mark Question',
            },
        ),
        migrations.CreateModel(
            name='Add_Question_2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': '2 Mark Questions',
                'verbose_name': '2 Mark Question',
            },
        ),
        migrations.CreateModel(
            name='Add_Question_3',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': '3 Mark Questions',
                'verbose_name': '3 Mark Question',
            },
        ),
        migrations.CreateModel(
            name='Add_Question_4',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': '4 Mark Questions',
                'verbose_name': '4 Mark Question',
            },
        ),
        migrations.CreateModel(
            name='Add_Question_5',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': '5 Mark Questions',
                'verbose_name': '5 Mark Question',
            },
        ),
        migrations.CreateModel(
            name='Add_Question_Fill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Fill in the Blanks Questions',
                'verbose_name': 'Fill in the blanks Question',
            },
        ),
        migrations.CreateModel(
            name='Add_Question_MCQ',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'MCQ Questions',
                'verbose_name': 'MCQ Question',
            },
        ),
        migrations.CreateModel(
            name='Ans_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=50)),
            ],
            options={
                'verbose_name_plural': '1 Mark Answers',
                'verbose_name': '1 Mark Answers',
            },
        ),
        migrations.CreateModel(
            name='Ans_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=100)),
            ],
            options={
                'verbose_name_plural': '2 Mark Answers',
                'verbose_name': '2 Mark Answer',
            },
        ),
        migrations.CreateModel(
            name='Ans_3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=550)),
            ],
            options={
                'verbose_name_plural': '3 Mark Answers',
                'verbose_name': '3 Mark Answer',
            },
        ),
        migrations.CreateModel(
            name='Ans_4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=2000)),
            ],
            options={
                'verbose_name_plural': '4 Mark Answers',
                'verbose_name': '4 Mark Answer',
            },
        ),
        migrations.CreateModel(
            name='Ans_5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=1000)),
            ],
            options={
                'verbose_name_plural': '5 Mark Answers',
                'verbose_name': '5 Mark Answer',
            },
        ),
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('assessment_id', models.AutoField(primary_key=True, serialize=False)),
                ('Duration', models.DurationField()),
                ('Type_of_assessment', models.CharField(choices=[('Q', 'Question'), ('C', 'Chapter'), ('S', 'Subject')], max_length=20)),
                ('issue_date', models.DateTimeField()),
                ('deadline_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='assessment_chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Assessment')),
            ],
        ),
        migrations.CreateModel(
            name='Assessment_Faculty',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('assessment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Assessment')),
            ],
        ),
        migrations.CreateModel(
            name='Assessment_group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('assessement_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Assessment')),
            ],
        ),
        migrations.CreateModel(
            name='assessment_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Assessment')),
            ],
        ),
        migrations.CreateModel(
            name='Assessment_Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Assessment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Assessment')),
            ],
        ),
        migrations.CreateModel(
            name='assessment_subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Assessment')),
            ],
        ),
        migrations.CreateModel(
            name='Assessment_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessment', models.CharField(choices=[('Q', 'Question'), ('C', 'Chapter'), ('S', 'Subject')], max_length=10)),
                ('assessment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Assessment')),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('chapter_id', models.AutoField(primary_key=True, serialize=False)),
                ('chapter_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Chapter_Resource',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('chapter_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Chapter')),
            ],
        ),
        migrations.CreateModel(
            name='City_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('Class_id', models.AutoField(primary_key=True, serialize=False)),
                ('Class_name', models.CharField(default=0, max_length=10)),
                ('board', models.CharField(choices=[('CBSE', 'Central Board of Secondary Education'), ('KTK', 'Karnataka Secondary Education Examination Board'), ('ICSE', 'Indian Certificate of Secondary Education')], max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='Class_Faculty',
            fields=[
                ('ss_id', models.AutoField(primary_key=True, serialize=False)),
                ('Class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Class')),
            ],
        ),
        migrations.CreateModel(
            name='District_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('District', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('faculty_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('designations', models.CharField(max_length=20)),
                ('Date_of_joining', models.DateField(default=None, verbose_name='Date of joining')),
                ('Class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty_School',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fac_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty_subject',
            fields=[
                ('ss_id', models.AutoField(primary_key=True, serialize=False)),
                ('faculty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Fill_Ans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=25)),
            ],
            options={
                'verbose_name_plural': 'Fill in the Blanks Answer',
                'verbose_name': 'Fill in the Blanks Answer',
            },
        ),
        migrations.CreateModel(
            name='MCQ_Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('correct_answer', models.CharField(choices=[('option_1', 'A'), ('option_2', 'B'), ('option_3', 'C'), ('option_4', 'D')], max_length=2)),
            ],
            options={
                'verbose_name_plural': 'MCQ Answers',
                'verbose_name': 'MCQ Answer',
            },
        ),
        migrations.CreateModel(
            name='MCQ_Options',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('option_1', models.CharField(max_length=25)),
                ('option_2', models.CharField(max_length=25)),
                ('option_3', models.CharField(max_length=25)),
                ('option_4', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('Person_id', models.AutoField(primary_key=True, serialize=False)),
                ('First_name', models.CharField(max_length=20)),
                ('Middle_name', models.CharField(max_length=20)),
                ('Last_name', models.CharField(max_length=20)),
                ('Street_Address', models.CharField(max_length=50)),
                ('Pincode', models.IntegerField(default=0)),
                ('DOB', models.DateField()),
                ('City', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.City_list')),
                ('District', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.District_list')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('q_id', models.AutoField(primary_key=True, serialize=False)),
                ('Q_type', models.CharField(choices=[('1M', '1 Mark'), ('2M', '2 Marks'), ('3M', '3 Marks'), ('5M', '5 Marks'), ('4M', '4 Marks'), ('Fill', 'Fill In The Blanks'), ('MCQ', 'Multiple Choice Question')], max_length=10)),
                ('question', models.TextField(default=None, max_length=100)),
                ('related_file', models.FileField(blank=True, null=True, upload_to=App.models.Question.upload_handler, verbose_name='Upload the Related Documents')),
                ('chap_id', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='sub_id', chained_model_field='sub_id', on_delete=django.db.models.deletion.CASCADE, to='App.Chapter')),
            ],
            options={
                'verbose_name_plural': 'Questions',
                'verbose_name': 'Question',
            },
        ),
        migrations.CreateModel(
            name='Question_Resource',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('res_id', models.AutoField(primary_key=True, serialize=False)),
                ('resource', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Resource_type',
            fields=[
                ('Resource_id', models.AutoField(primary_key=True, serialize=False)),
                ('Type', models.CharField(choices=[('Q', 'Question'), ('C', 'Chapter'), ('S', 'Subject')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('assessments_results_id', models.AutoField(primary_key=True, serialize=False)),
                ('Grade', models.CharField(max_length=10)),
                ('assessment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Assessment')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('School_id', models.AutoField(primary_key=True, serialize=False)),
                ('school_name', models.CharField(max_length=40)),
                ('Street_Address', models.CharField(max_length=50)),
                ('Contact_Number', models.IntegerField()),
                ('City', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.City_list')),
                ('District', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.District_list')),
                ('HM_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Staff_Visitors',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('permission_group', models.CharField(max_length=10)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Person')),
            ],
        ),
        migrations.CreateModel(
            name='State_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('medium', models.CharField(choices=[('K', 'Kannada'), ('E', 'English'), ('H', 'Hindi')], max_length=10)),
                ('board', models.CharField(choices=[('CBSE', 'Central Board of Secondary Education'), ('KTK', 'Karnataka Secondary Education Examination Board'), ('ICSE', 'Indian Certificate of Secondary Education')], max_length=24)),
                ('Person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Person')),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.School')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Faculty',
            fields=[
                ('ss_id', models.AutoField(primary_key=True, serialize=False)),
                ('faculty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Faculty')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Student_group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('group_id', models.CharField(max_length=20)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('sub_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_name', models.CharField(max_length=20)),
                ('class_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='App.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Subject_Resource',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('resource_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Resource')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Taluk_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taluk', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='school',
            name='State',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.State_list'),
        ),
        migrations.AddField(
            model_name='school',
            name='Taluk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Taluk_list'),
        ),
        migrations.AddField(
            model_name='results',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Student'),
        ),
        migrations.AddField(
            model_name='resource',
            name='type_res',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Resource_type'),
        ),
        migrations.AddField(
            model_name='question_resource',
            name='resource_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Resource'),
        ),
        migrations.AddField(
            model_name='question',
            name='sub_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Subject'),
        ),
        migrations.AddField(
            model_name='person',
            name='State',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.State_list'),
        ),
        migrations.AddField(
            model_name='person',
            name='Taluk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Taluk_list'),
        ),
        migrations.AddField(
            model_name='mcq_options',
            name='quest_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Question'),
        ),
        migrations.AddField(
            model_name='mcq_answer',
            name='options_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.MCQ_Options'),
        ),
        migrations.AddField(
            model_name='mcq_answer',
            name='quest_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Question'),
        ),
        migrations.AddField(
            model_name='fill_ans',
            name='quest_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Question'),
        ),
        migrations.AddField(
            model_name='faculty_subject',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Subject'),
        ),
        migrations.AddField(
            model_name='faculty_school',
            name='sch_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.School'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='Person_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Person'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Subject'),
        ),
        migrations.AddField(
            model_name='class_faculty',
            name='faculty_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Faculty'),
        ),
        migrations.AddField(
            model_name='chapter_resource',
            name='resource_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Resource'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='sub_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='App.Subject'),
        ),
        migrations.AddField(
            model_name='assessment_subject',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Subject'),
        ),
        migrations.AddField(
            model_name='assessment_student',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Student'),
        ),
        migrations.AddField(
            model_name='assessment_question',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Question'),
        ),
        migrations.AddField(
            model_name='assessment_group',
            name='group_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Student_group'),
        ),
        migrations.AddField(
            model_name='assessment_faculty',
            name='faculty_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Faculty'),
        ),
        migrations.AddField(
            model_name='assessment_chapter',
            name='chapter_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Question'),
        ),
        migrations.AddField(
            model_name='assessment',
            name='faculty_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Faculty'),
        ),
        migrations.AddField(
            model_name='ans_5',
            name='quest_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Question'),
        ),
        migrations.AddField(
            model_name='ans_4',
            name='quest_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Question'),
        ),
        migrations.AddField(
            model_name='ans_3',
            name='quest_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Question'),
        ),
        migrations.AddField(
            model_name='ans_2',
            name='quest_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Question'),
        ),
        migrations.AddField(
            model_name='ans_1',
            name='quest_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Question'),
        ),
    ]