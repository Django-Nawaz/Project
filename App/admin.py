from django.contrib import admin
from .models import *
from django import forms
admin.site.register([Class,Chapter,MCQ_Answer])

admin.site.site_header = 'Data Entry Portal'
admin.site.site_title = ' '
admin.site.index_title = 'Data Entry For Content Developers'


    
admin.site.register([Sub_Units,Concepts])



class Question_Admin(admin.ModelAdmin):
    def type_of_question(self,obj):
        return str(obj.get_Q_type_display())
    def Board(self,obj):
        return (obj.sub_id.class_id.get_board_display())
        
    list_display = ('question','type_of_question','sub_id','Board','related_file')
    list_filter = ('sub_id','sub_id__sub_name','sub_id__class_id__board')
    search_fields = ('question',)
    
       
admin.site.register(Question,Question_Admin)
class Subject_Admin(admin.ModelAdmin):
        
    #list_display = ('sub_name','class_id__Class_name','class_id__board')
    list_filter = ('sub_name','class_id__board',)
    search_fields = ('class_id__Class_name',)
admin.site.register(Subject,Subject_Admin)   

class One_Marks_Question(Question):
    class Meta:
        verbose_name = '1 Marks Question'
        verbose_name_plural = '1 Marks Questions'
        proxy = True
    
class One_Marks_Question_Form(forms.ModelForm):
    Answer = forms.Field(widget=forms.widgets.TextInput)
    explaination = forms.Field(widget=forms.widgets.Textarea)
    class Meta:
        model = One_Marks_Question
        fields = '__all__'
        exclude = ['Q_type',]
    def save(self,commit=False):
        instance = super(One_Marks_Question_Form, self).save(commit=False)
        instance.Q_type = '1M'
        instance.save()
        
        obj_ans = Ans_1(answer = self.cleaned_data['Answer'],quest_id = instance)
        obj_ans.save()
        print("Saving 1 Marks Question")
        return instance
class Admin_One(admin.ModelAdmin):
    form = One_Marks_Question_Form
    fieldsets = (
    ('Enter Subject Chapter Sub-Unit Below',
     {'fields':('sub_id','chap_id','sub_unit','concept',)}),    
    ('Enter Question and Answer',{'fields':('question','Answer')}),
    ('Other Related Informations Below',{'classes':('collapse',),'fields':('related_file','related_file_answer','explaination')})
    )
    def Answer(self,obj):
        Obj = Ans_1.objects.get(quest_id = obj)
        return str(Obj.answer)
    list_display = ('question','Answer',)
    def get_queryset(self,request):
        return Question.objects.filter(Q_type='1M')
        
admin.site.register(One_Marks_Question,Admin_One)


class Two_Marks_Question(Question):
    class Meta:
        verbose_name = '2 Marks Question'
        verbose_name_plural = '2 Marks Questions'
        proxy = True       
class Two_Marks_Question_Form(forms.ModelForm):
    Answer = forms.Field(required=True,widget=forms.widgets.Textarea)
    class Meta:
        model = Two_Marks_Question
        fields = '__all__'
        exclude = ['Q_type',]
    def save(self,commit=False):
        instance = super(Two_Marks_Question_Form, self).save(commit=False)
        instance.Q_type = '2M'
        instance.save()
        obj_ans = Ans_2(answer = self.cleaned_data['Answer'],quest_id = instance)
        obj_ans.save()
        print("Saving 2 Marks Question")
        return instance
class Admin_Two(admin.ModelAdmin):
    form = Two_Marks_Question_Form
    fieldsets = (
    ('Enter Subject Chapter Sub-Unit Below',
     {'fields':('sub_id','chap_id','sub_unit','concept',)}),    
    ('Enter Question and Answer',{'fields':('question','Answer')}),
    ('Other Related Informations Below',{'classes':('collapse',),'fields':('related_file','related_file_answer','explaination')})
    )
    def Answer(self,obj):
        Obj = Ans_2.objects.get(quest_id = obj)
        return str(Obj.answer)
    list_display = ('question','Answer',)
    def get_queryset(self,request):
        return Question.objects.filter(Q_type='2M')
admin.site.register(Two_Marks_Question,Admin_Two)

class Three_Marks_Question(Question):
    class Meta:
        verbose_name = '3 Marks Question'
        verbose_name_plural = '3 Marks Questions'
        proxy = True       
class Three_Marks_Question_Form(forms.ModelForm):
    Answer = forms.Field(required=True,widget=forms.widgets.Textarea)
    class Meta:
        model = Three_Marks_Question
        fields = '__all__'
        exclude = ['Q_type',]
    def save(self,commit=False):
        instance = super(Three_Marks_Question_Form, self).save(commit=False)
        instance.Q_type = '3M'
        instance.save()
        
        obj_ans = Ans_3(answer = self.cleaned_data['Answer'],quest_id = instance)
        obj_ans.save()
        print("Saving 3 Marks Question")
        return instance
class Admin_Three(admin.ModelAdmin):
    form = Three_Marks_Question_Form
    fieldsets = (
    ('Enter Subject Chapter Sub-Unit Below',
     {'fields':('sub_id','chap_id','sub_unit','concept',)}),    
    ('Enter Question and Answer',{'fields':('question','Answer')}),
    ('Other Related Informations Below',{'classes':('collapse',),'fields':('related_file','related_file_answer','explaination')})
    )
    def Answer(self,obj):
        Obj = Ans_3.objects.get(quest_id = obj)
        return str(Obj.answer)
    list_display = ('question','Answer',)
    def get_queryset(self,request):
        return Question.objects.filter(Q_type='3M')
admin.site.register(Three_Marks_Question,Admin_Three)
class Four_Marks_Question(Question):
    class Meta:
        verbose_name = '4 Marks Question'
        verbose_name_plural = '4 Marks Questions'
        proxy = True  
class Four_Marks_Question_Form(forms.ModelForm):
    Answer = forms.Field(required=True,widget=forms.widgets.Textarea)
    class Meta:
        model = Four_Marks_Question
        fields = '__all__'
        exclude = ['Q_type',]
    def save(self,commit=False):
        instance = super(Four_Marks_Question_Form, self).save(commit=False)
        instance.Q_type = '4M'        
        instance.save()
        obj_ans = Ans_4(answer = self.cleaned_data['Answer'],quest_id = instance)
        obj_ans.save()
        print("Saving 4 Marks Question")
        return instance
class Admin_Four(admin.ModelAdmin):
    form = Four_Marks_Question_Form
    fieldsets = (
    ('Enter Subject Chapter Sub-Unit Below',
     {'fields':('sub_id','chap_id','sub_unit','concept',)}),    
    ('Enter Question and Answer',{'fields':('question','Answer')}),
    ('Other Related Informations Below',{'classes':('collapse',),'fields':('related_file','related_file_answer','explaination')})
    )
    def Answer(self,obj):
        Obj = Ans_4.objects.get(quest_id = obj)
        return str(Obj.answer)
    list_display = ('question','Answer',)
    def get_queryset(self,request):
        return Question.objects.filter(Q_type='4M')
admin.site.register(Four_Marks_Question,Admin_Four)
class Five_Marks_Question(Question):
    class Meta:
        verbose_name = '5 Marks Question'
        verbose_name_plural = '5 Marks Questions'
        proxy = True  

class Five_Marks_Question_Form(forms.ModelForm):
    Answer = forms.Field(required=True,widget=forms.widgets.Textarea)
    class Meta:
        model = Five_Marks_Question
        fields = '__all__'
        exclude = ['Q_type',]
    def save(self,commit=False):
        instance = super(Five_Marks_Question_Form, self).save(commit=False)
        instance.Q_type = '5M'        
        instance.save()
        obj_ans = Ans_5(answer = self.cleaned_data['Answer'],quest_id = instance)
        obj_ans.save()
        print("Saving 5 Marks Question")
        return instance
class Admin_Five(admin.ModelAdmin):
    fieldsets = (
    ('Enter Subject Chapter Sub-Unit Below',
     {'fields':('sub_id','chap_id','sub_unit','concept',)}),    
    ('Enter Question and Answer',{'fields':('question','Answer')}),
    ('Other Related Informations Below',{'classes':('collapse',),'fields':('related_file','related_file_answer','explaination')})
    )
    form = Five_Marks_Question_Form
    def Answer(self,obj):
        Obj = Ans_5.objects.get(quest_id = obj)
        return str(Obj.answer)
    list_display = ('question','Answer',)
    def get_answer(self,obj):
        try:    
            answer = Ans_5.objects.get(quest_id = obj)
        except Exception as e:
            return "Multiple Answers Are There"
        return str(answer)
    get_answer.short_description = "Answer"
    list_display = ('question','get_answer')
    def get_queryset(self,request):
        return Question.objects.filter(Q_type='5M')
admin.site.register(Five_Marks_Question,Admin_Five) 
#########################
class Fill_Question(Question):
    class Meta:
        verbose_name = 'A Fill in The Blank Question'
        verbose_name_plural = 'Fill in The Blank Questions'
        proxy = True  

class Fill_Marks_Question_Form(forms.ModelForm):
    Answer = forms.Field(required=True,widget=forms.widgets.TextInput)
    class Meta:
        model = Fill_Question
        fields = '__all__'
        exclude = ['Q_type',]
    def save(self,commit=False):
        instance = super(Fill_Marks_Question_Form, self).save(commit=False)
        instance.Q_type = 'Fill'        
        instance.save()
        obj_ans = Fill_Ans(answer = self.cleaned_data['Answer'],quest_id = instance)
        obj_ans.save()
        print("Saving Fill in the Blanks Question")
        return instance
class Admin_Fill(admin.ModelAdmin):
    fieldsets = (
    ('Enter Subject Chapter Sub-Unit Below',
     {'fields':('sub_id','chap_id','sub_unit','concept',)}),    
    ('Enter Question and Answer',{'fields':('question','Answer')}),
    ('Other Related Informations Below',{'classes':('collapse',),'fields':('related_file','related_file_answer','explaination')})
    )
    form = Fill_Marks_Question_Form
    def Answer(self,obj):
        Obj = Fill_Ans.objects.get(quest_id = obj)
        return str(Obj.answer)
    list_display = ('question','Answer',)
    list_display = ('question','sub_id','related_file')
    def get_queryset(self,request):
        return Question.objects.filter(Q_type='Fill')
admin.site.register(Fill_Question,Admin_Fill)


class MCQ_Marks_Question(Question):
    class Meta:
        verbose_name = 'Multiple Choice Question'
        verbose_name_plural = 'Multiple Choice Questions'
        proxy = True  

class MCQ_Marks_Question_Form(forms.ModelForm):
    option_1 = forms.Field(required=True,widget=forms.widgets.TextInput,label = 'Choice A')
    option_2 = forms.Field(required=True,widget=forms.widgets.TextInput,label = 'Choice B')
    option_3 = forms.Field(required=True,widget=forms.widgets.TextInput,label = 'Choice C')
    option_4 = forms.Field(required=True,widget=forms.widgets.TextInput,label = 'Choice D')
    Answer = forms.Field(label = 'Select the Answer Choice',required=True,widget = forms.widgets.Select(choices = (('option_1','A'),('option_2','B'),('option_3','C'),('option_4','D'))))
    
    class Meta:
        model = MCQ_Marks_Question
        fields = '__all__'
        exclude = ['Q_type',]
    def save(self,commit=False):
        instance = super(MCQ_Marks_Question_Form, self).save(commit=False)
        instance.Q_type = 'MCQ'        
        instance.save()
        data = self.cleaned_data
        obj_options = MCQ_Options(quest_id = instance,option_1 = data['option_1'],option_2 = data['option_2'],option_3 = data['option_3'],option_4 = data['option_4'])
        obj_options.save()
        obj_ans = MCQ_Answer(correct_answer = self.cleaned_data['Answer'],quest_id = instance,options_id = obj_options)
        obj_ans.save()
        print("Saving MCQ Marks Question")
        return instance
#admin.site.register(MCQ_Options)
class Admin_MCQ(admin.ModelAdmin):
    form = MCQ_Marks_Question_Form
    fieldsets = (
    ('Enter Subject Chapter Sub-Unit Below',
     {'fields':('sub_id','chap_id','sub_unit','concept',)}),    
    ('Enter Question and Answer',{'fields':('question','option_1','option_2','option_3','option_4','Answer')}),
    ('Other Related Informations Below',{
    'classes':('collapse',),
    'fields':('related_file','related_file_answer','explaination')})
    )
    def Answer(self,obj):
        Obj = MCQ_Answer.objects.get(quest_id = obj)
        return str(Obj.answer)
    list_display = ('question','Answer','Answer')

    def get_answer(self,obj):
        try:    
            answer = MCQ_Answer.objects.get(quest_id = obj)
            if str(answer)=='option_1':
                ans = MCQ_Options.objects.get(quest_id = obj)
                return str(ans.option_1)
            if str(answer)=='option_2':
                ans = MCQ_Options.objects.get(quest_id = obj)
                return str(ans.option_2)
            if str(answer)=='option_3':
                ans = MCQ_Options.objects.get(quest_id = obj)
                return str(ans.option_3)
            if str(answer)=='option_4':
                ans = MCQ_Options.objects.get(quest_id = obj)
                return str(ans.option_4)
        except Exception as e:
            return "Multiple Answers Are There"
        return str(answer)
    get_answer.short_description = "Answer"
    list_display = ('question','get_answer')
    def get_queryset(self,request):
        return Question.objects.filter(Q_type='MCQ')
admin.site.register(MCQ_Marks_Question,Admin_MCQ)


   
# Register your models here.
