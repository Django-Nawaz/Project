from django.db import models
MEDIUM_CHOICES = (('K','Kannada'),('E','English'),('H','Hindi'),)
BOARD_CHOICES =(('CBSE','Central Board of Secondary Education'),('KTK','Karnataka Secondary Education Examination Board'),
('ICSE','Indian Certificate of Secondary Education'),)



Question_Choices = (('1M','1 Mark'),('2M','2 Marks'),('3M','3 Marks'),('5M','5 Marks'),('4M','4 Marks'),('Fill','Fill In The Blanks'),('MCQ','Multiple Choice Question'))

class City_list(models.Model):
    city = models.CharField(max_length=20)
    def __str__(self):
        return self.city
        
class Taluk_list(models.Model):
    taluk = models.CharField(max_length=20)
    def __str__(self):
        return self.taluk
    
class District_list(models.Model):
    District = models.CharField(max_length=20)
    def __str__(self):
        return self.District
        
class State_list(models.Model):
    state = models.CharField(max_length=20)
    def __str__(self):
        return self.state

    
class Person(models.Model):
    Person_id = models.AutoField(primary_key = True)
    First_name = models.CharField(max_length=20)
    Middle_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    Street_Address = models.CharField(max_length=50)
    City = models.ForeignKey(City_list)
    Taluk = models.ForeignKey(Taluk_list)
    District = models.ForeignKey(District_list)
    State = models.ForeignKey(State_list)
    Pincode = models.IntegerField(default=0)
    DOB = models.DateField()
    def __str__(self):
        return self.First_name+' '+self.Middle_name+' '+self.Last_name
        


class School(models.Model):
    School_id = models.AutoField(primary_key=True)
    HM_id = models.ForeignKey(Person)
    school_name = models.CharField(max_length=40)
    Street_Address = models.CharField(max_length=50)
    City = models.ForeignKey(City_list)
    Taluk = models.ForeignKey(Taluk_list)
    District = models.ForeignKey(District_list)
    State = models.ForeignKey(State_list)
    Contact_Number = models.IntegerField()
    def __str__(self):
        return self.school_name+', '+self.Taluk
        

class Student(models.Model):
    Person_id = models.ForeignKey(Person)
    student_id = models.CharField(max_length=20,primary_key = True)
    school_id = models.ForeignKey(School)
    medium = models.CharField(max_length=10,choices = MEDIUM_CHOICES)
    board = models.CharField(max_length=24,choices = BOARD_CHOICES)
    def __str__(self):
        return self.student_id
        

    
class Class(models.Model):    
    Class_id = models.AutoField(primary_key = True)
    Class_name = models.CharField(default=0,max_length=10)
    board = models.CharField(max_length=24,choices = BOARD_CHOICES)
    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'       
    def __str__(self):
        return self.Class_name

        
class Faculty(models.Model):
    Person_id = models.ForeignKey(Person)
    faculty_id = models.CharField(primary_key=True,max_length=20)
    Class_id = models.ForeignKey(Class)
    subject_id = models.ForeignKey('App.Subject')
    designations = models.CharField(max_length=20)
    Date_of_joining = models.DateField('Date of joining', default=None)
    def __str__(self):
        return self.faculty_id
        
class Faculty_School(models.Model):
    id = models.AutoField(primary_key = True)
    fac_id = models.ForeignKey(Faculty)
    sch_id = models.ForeignKey(School)
    
class Staff_Visitors(models.Model):
    id = models.AutoField(primary_key = True)
    staff_id = models.ForeignKey(Person)
    permission_group = models.CharField(max_length=10)
    
class Subject(models.Model):
    sub_id = models.AutoField(primary_key = True)
    sub_name = models.CharField(max_length=20)
    class_id = models.ForeignKey(Class,default = None)
    def __str__(self):
        return str(self.class_id.Class_name+'th '+ self.sub_name)
        
    
class Chapter(models.Model):
    chapter_id = models.AutoField(primary_key = True)
    chapter_name = models.CharField(max_length=20)
    sub_id = models.ForeignKey('App.Subject',default = None)
    class Meta:
        verbose_name = 'Chapter'
        verbose_name_plural = 'Chapters'
    def __str__(self):
        return self.chapter_name
from smart_selects.db_fields import ChainedForeignKey
class Sub_Units(models.Model):
    sub_id = models.ForeignKey(Subject)
    chap_id = ChainedForeignKey(Chapter,chained_field='sub_id',chained_model_field='sub_id',show_all=False,auto_choose=True,sort=True)
    sub_unit = models.CharField(max_length = 40)
    class Meta:
        verbose_name = 'Sub Unit'
        verbose_name_plural = 'Sub Units'
    def __str__(self):
        return str(self.sub_unit)
class Concepts(models.Model):
    sub_id = models.ForeignKey(Subject)
    chap_id = ChainedForeignKey(Chapter,chained_field='sub_id',chained_model_field='sub_id',show_all=False,auto_choose=True,sort=True)
    sub_unit_id = ChainedForeignKey(Sub_Units,chained_field='chap_id',chained_model_field='chap_id',show_all=False,auto_choose=True,sort=True)
    concept = models.CharField(max_length = 40)
    class Meta:
        verbose_name = 'Concept'
        verbose_name_plural = 'Concepts'
    def __str__(self):
        return str(self.concept)
import os

class Question(models.Model):
    
    def upload_handler(instance,filename):
        upload_dir = os.path.join('media',str(instance.sub_id))
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)   
        upload_sub_dir = os.path.join(upload_dir,str(instance.chap_id))
        if not os.path.exists(upload_sub_dir):
            os.makedirs(upload_sub_dir)
            
        upload_sub_ques = os.path.join(upload_sub_dir,str(instance.Q_type))
        if not os.path.exists(upload_sub_ques):
            os.makedirs(upload_sub_ques)
        print(os.path.join(upload_sub_ques, filename))
        return os.path.join(upload_sub_ques, filename)
    #hint = models.CharField(max_length = 35,verbose_name = "Hint to the Question")    
    q_id = models.AutoField(primary_key = True)
    Q_type = models.CharField(choices =Question_Choices ,max_length = 10)
    sub_id = models.ForeignKey('App.Subject',verbose_name = 'Subject ')
    chap_id = ChainedForeignKey(Chapter,verbose_name = 'Chapter ',chained_field='sub_id',chained_model_field='sub_id',show_all=False,auto_choose=True,sort=True)
    sub_unit = ChainedForeignKey(Sub_Units,verbose_name = 'Sub-Unit ',chained_field='chap_id',chained_model_field='chap_id',show_all=False,auto_choose=True,sort=True)
    concept = ChainedForeignKey(Concepts,verbose_name = 'Concept ',chained_field='sub_unit',chained_model_field='sub_unit_id',show_all=False,auto_choose=True,sort=True)
    question = models.TextField(verbose_name = 'Question ',max_length=100,default = None)
    related_file = models.FileField(verbose_name = "Upload the Related Question Documents",blank=True,null = True,upload_to = upload_handler)
    related_file_answer = models.FileField(verbose_name = "Upload the Answer Documents",blank=True,null = True,upload_to = upload_handler)
    explaination = models.TextField('Explaination',max_length = 500,null = True,blank = True,default = "No Explaination")    
    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
    def __str__(self):
        return str(self.question)
class Ans_1(models.Model):
    answer = models.TextField(max_length=50)
    quest_id = models.ForeignKey(Question)  
    class Meta:
        verbose_name = '1 Mark Answers'
        verbose_name_plural = '1 Mark Answers'
        
    def __str__(self):
        return str(self.quest_id)
        
class Ans_2(models.Model):
    answer = models.TextField(max_length=100)
    quest_id = models.ForeignKey(Question)  
    class Meta:
        verbose_name = '2 Mark Answer'
        verbose_name_plural = '2 Mark Answers'
    def __str__(self):
        return str(self.quest_id)
class Ans_3(models.Model):
    answer = models.TextField(max_length=550)
    quest_id = models.ForeignKey(Question)
    class Meta:
        verbose_name = '3 Mark Answer'
        verbose_name_plural = '3 Mark Answers'
    def __str__(self):
        return str(self.quest_id)
class Ans_5(models.Model):
    answer = models.TextField(max_length=1000)
    quest_id = models.ForeignKey(Question)
    def __str__(self):
        return str(self.quest_id)
    class Meta:
        verbose_name = '5 Mark Answer'
        verbose_name_plural = '5 Mark Answers'
class Ans_4(models.Model):
    answer = models.TextField(max_length=2000)
    quest_id = models.ForeignKey(Question)
    class Meta:
        verbose_name = '4 Mark Answer'
        verbose_name_plural = '4 Mark Answers'
    def __str__(self):
        return str(self.id)
        
class Fill_Ans(models.Model):
    answer = models.TextField(max_length=25)
    quest_id = models.ForeignKey(Question)
    class Meta:
        verbose_name = 'Fill in the Blanks Answer'
        verbose_name_plural = 'Fill in the Blanks Answer'
    def __str__(self):
        return str(self.id)            
class MCQ_Options(models.Model):
    id = models.AutoField(primary_key = True)
    quest_id = models.ForeignKey(Question)
    option_1 = models.CharField(max_length=25)
    option_2 = models.CharField(max_length=25)
    option_3 = models.CharField(max_length=25)
    option_4 = models.CharField(max_length=25)
    def __str__(self):
        return str(self.id)
    
class MCQ_Answer(models.Model):
    id = models.AutoField(primary_key = True)
    quest_id = models.ForeignKey(Question)
    options_id = models.ForeignKey(MCQ_Options)
    correct_answer = models.CharField(choices = (('option_1','A'),('option_2','B'),('option_3','C'),('option_4','D')),max_length=10)
    class Meta:
        verbose_name = 'MCQ Answer'
        verbose_name_plural = 'MCQ Answers'
    def __str__(self):
        return str(self.correct_answer)    
    
class Assessment(models.Model):
    assessment_id = models.AutoField(primary_key = True)
    faculty_id = models.ForeignKey(Faculty)
    Duration = models.DurationField()
    Type_of_assessment = models.CharField(choices = (('Q','Question'),('C','Chapter'),('S','Subject')),max_length=20)
    issue_date = models.DateTimeField()
    deadline_date = models.DateTimeField()
    def __str__(self):
        return self.Type_of_assessment+' '+self.assessment_id
    
    
class Student_group(models.Model):
    id = models.AutoField(primary_key = True)
    group_id = models.CharField(max_length = 20)
    student_id = models.ForeignKey(Student)
    def __str__(self):
        return self.group_id
    
class Results(models.Model):
    assessments_results_id = models.AutoField(primary_key=True)
    assessment_id = models.ForeignKey(Assessment)    
    student_id = models.ForeignKey(Student)
    Grade = models.CharField(max_length=10)
    def __str__(self):
        return self.assessment_id+' '+self.student_id
    
class Student_Faculty(models.Model):
    ss_id = models.AutoField(primary_key = True)
    student_id = models.ForeignKey(Student)
    faculty_id = models.ForeignKey(Faculty)
    def __str__(self):
        return self.ss_id
class Faculty_subject(models.Model):
    ss_id = models.AutoField(primary_key = True)
    subject_id = models.ForeignKey(Subject)
    faculty_id = models.ForeignKey(Faculty)
    def __str__(self):
        return self.ss_id


class Class_Faculty(models.Model):
    ss_id = models.AutoField(primary_key = True)
    Class_id = models.ForeignKey(Class)
    faculty_id = models.ForeignKey(Faculty)
    def __str__(self):
        return self.ss_id
class Assessment_Faculty(models.Model):
    id = models.AutoField(primary_key = True)
    assessment_id = models.ForeignKey(Assessment)
    faculty_id = models.ForeignKey(Faculty)
    def __str__(self):
        return self.id
    
class Assessment_Student(models.Model):
    id = models.AutoField(primary_key = True) 
    Assessment_id = models.ForeignKey(Assessment)
    student_id = models.ForeignKey(Student)    
    def __str__(self):
        return str(self.id)
    
class Assessment_group(models.Model):
    id = models.AutoField(primary_key = True)
    group_id = models.ForeignKey(Student_group)
    assessement_id = models.ForeignKey(Assessment)
    def __str__(self):
        return str(self.id)
        
class Resource_type(models.Model):
    Resource_id = models.AutoField(primary_key = True)
    Type = models.CharField(max_length = 10,choices = (('Q','Question'),('C','Chapter'),('S','Subject')))                                        #type of resource
    def __str__(self):
        return str(self.Resource_id)
    
class Resource(models.Model):
    res_id = models.AutoField(primary_key = True)
    resource = models.CharField(max_length = 100)
    type_res = models.ForeignKey(Resource_type)
    def __str__(self):
        return str(self.res_id)


    
class Subject_Resource(models.Model):  
    id = models.AutoField(primary_key = True)
    resource_id = models.ForeignKey(Resource)
    subject_id = models.ForeignKey(Subject)
    def __str__(self):
        return str(self.id)
    
class Chapter_Resource(models.Model):
    id = models.AutoField(primary_key = True)
    resource_id = models.ForeignKey(Resource)
    chapter_id = models.ForeignKey(Chapter)    
    def __str__(self):
        return str(self.id)

    
class Question_Resource(models.Model):
     
     id = models.AutoField(primary_key = True)
     resource_id = models.ForeignKey(Resource)
     question_id = models.ForeignKey(Question) 
     def __str__(self):
        return str(self.id)


     
            
class assessment_subject(models.Model):
    assessment_id = models.ForeignKey(Assessment)
    subject_id = models.ForeignKey(Subject)
    def __str__(self):
        return str(self.id)
        
class assessment_chapter(models.Model):
    assessment_id = models.ForeignKey(Assessment)
    chapter_id = models.ForeignKey(Question)

class assessment_Question(models.Model):
    assessment_id = models.ForeignKey(Assessment)
    question_id = models.ForeignKey(Question)    
    
class Assessment_Type(models.Model):
    assessment_id = models.ForeignKey(Assessment)
    assessment = models.CharField(max_length=10,choices = (('Q','Question'),('C','Chapter'),('S','Subject')))
    
        
    
class Add_Question_1(models.Model):
    id = models.AutoField(primary_key = True)
    
    class Meta:
        verbose_name = '1 Mark Question'
        verbose_name_plural = '1 Mark Questions'
        

class Add_Question_2(models.Model):
    id = models.AutoField(primary_key = True)
    class Meta:
        verbose_name = '2 Mark Question'
        verbose_name_plural = '2 Mark Questions'
    
class Add_Question_3(models.Model):
    id = models.AutoField(primary_key = True)
    class Meta:
        verbose_name = '3 Mark Question'
        verbose_name_plural = '3 Mark Questions'
class Add_Question_5(models.Model):
    id = models.AutoField(primary_key = True)
    class Meta:
        verbose_name = '5 Mark Question'
        verbose_name_plural = '5 Mark Questions'
        
class Add_Question_4(models.Model):
    id = models.AutoField(primary_key = True)
    class Meta:
        verbose_name = '4 Mark Question'
        verbose_name_plural = '4 Mark Questions'
class Add_Question_MCQ(models.Model):
    id = models.AutoField(primary_key = True)
    class Meta:
        verbose_name = 'MCQ Question'
        verbose_name_plural = 'MCQ Questions'
class Add_Question_Fill(models.Model):
    id = models.AutoField(primary_key = True)
    class Meta:
        verbose_name = 'Fill in the blanks Question'
        verbose_name_plural = 'Fill in the Blanks Questions'

# Create your models here.
