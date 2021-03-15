from django.contrib import admin
from .models import *
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Unregister the provided model admin
admin.site.unregister(User)

# Register out own model admin, based on the default UserAdmin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display=['username','email','view_ids_link']


    def view_ids_link(self, obj):

        url = (
        urlencode({"year__id": f"{obj.id}"})
        )
        return obj.id

    view_ids_link.short_description = "Id"
# Register your models here.

@admin.register(LanguageSelector)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['lang_name','view_ids_link']
    readonly_fields = ['id']

    def view_ids_link(self, obj):

        # url = (
        # urlencode({"languageselector__id": f"{obj.id}"})
        # )
        return obj.id

    view_ids_link.short_description = "Id"


@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = ['policy_no', 'policy_title']
    list_filter = ['policy_no', 'show']


@admin.register(FAQ)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['faq_no', 'faq_question']
    list_filter = ['faq_no', 'show']


@admin.register(FAQSSCChsl)
class FaqSSCAdmin(admin.ModelAdmin):
    list_display = ['faq_no', 'faq_question']
    list_filter = ['faq_no', 'show']


@admin.register(TermsCondition)
class TermsConditionAdmin(admin.ModelAdmin):
    list_display = ['term_no', 'term_title']
    list_filter = ['term_no', 'show']


@admin.register(PreviousYear)
class PreviousYearAdmin(admin.ModelAdmin):
    list_display = ['year']


@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ['year','view_ids_link']


    def view_ids_link(self, obj):

        url = (
        urlencode({"year__id": f"{obj.id}"})
        )
        return obj.id

    view_ids_link.short_description = "Id"

@admin.register(Month)
class MonthAdmin(admin.ModelAdmin):
    list_display = ['month','view_ids_link']


    def view_ids_link(self, obj):

        url = (
        urlencode({"month__id": f"{obj.id}"})
        )
        return obj.id

    view_ids_link.short_description = "Id"

@admin.register(TestCategory)
class TestCategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'keyword', 'preview_keyword','view_ids_link']

    def view_ids_link(self, obj):

        url = (
        urlencode({"testcategory__id": f"{obj.id}"})
        )
        return obj.id

    view_ids_link.short_description = "Id"



@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject','view_ids_link']

    def view_ids_link(self, obj):

        url = (
        urlencode({"subject__id": f"{obj.id}"})
        )
        return obj.id

    view_ids_link.short_description = "Id"


@admin.register(TestName)
class TestNameAdmin(admin.ModelAdmin):
    list_display = ['test_name', 'category']
    search_fields = ['test_name', 'category', 'keyword']
    list_filter = ['month', 'year', 'is_previous_year_question', 'category']


# storage info models registered here


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ['info_title', 'month', 'year']
    search_fields = ['month', 'info_title', 'meassage']
    list_filter = ['year', 'month']

# Article info models are here


@admin.register(ArticleInfo)
class ArticleInfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'info_no', 'view_points_link']
    search_fields = ['title']
    list_filter = ['year', 'month', 'category', 'show']

    def view_points_link(self, obj):

        url = (
            reverse("admin:mockapp_jobinfopoints_changelist")
            + "?"
            + urlencode({"job_info__id": f"{obj.id}"})
        )
        return format_html('<a href="{}"> Points</a>', url)

    view_points_link.short_description = "Points"


@admin.register(ArticleInfoPoints)
class ArticleInfoPointsAdmin(admin.ModelAdmin):
    list_display = ['title', 'point_no']

# Job Info and points models are here


@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'keyword', 'preview_keyword']


@admin.register(JobInfo)
class JobInfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'info_no','view_points_link']
    search_fields = ['title']
    list_filter = ['year', 'month', 'category', 'show']


    def view_points_link(self,obj):
        url=(
            reverse("admin:mockapp_jobinfopoints_changelist")
            +"?"
            +urlencode({"job_info__id":f"{obj.id}"})
        )
        return format_html('<a href="{}">Points </a>',url)
    view_points_link.short_description = "Points"
   

@admin.register(JobInfoPoints)
class JobInfoPointsAdmin(admin.ModelAdmin):
    list_display = ['title', 'point_no']

#Institute models here
@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display=['name']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display=['name']

@admin.register(Institute)
class InstitueAdmin(admin.ModelAdmin):
    list_display=['name','added_by','city','state','view_ids_link'] 

    def view_ids_link(self, obj):

        url = (
        urlencode({"biharpolicetestname__id": f"{obj.id}"})
        )
        return obj.id  

    def get_queryset(self, request):
            qs = super().get_queryset(request)
            if request.user.is_superuser:
                return qs
            return qs.filter(added_by=request.user)

@admin.register(InstittuteOperator)
class InstittuteOperatorAdmin(admin.ModelAdmin):
    list_display=['name','city','state','view_ids_link']
    list_filter=['city','state']

    def view_ids_link(self, obj):

        url = (
        urlencode({"biharpolicetestname__id": f"{obj.id}"})
        )
        return obj.id  

    def get_queryset(self, request):
            qs = super().get_queryset(request)
            if request.user.is_superuser:
                return qs
            return qs.filter(added_by=request.user)

@admin.register(InstituteTestName)
class InstituteTestNameAdmin(admin.ModelAdmin):
    list_display=['test_name','city','state','view_ids_link']
    list_filter=['city','state','institute']

    def view_ids_link(self, obj):

        url = (
        urlencode({"institutetestname__id": f"{obj.id}"})
        )
        return obj.id  


    def view_question_link(self, obj):

        url = (
            reverse("admin:mockapp_questioninstitute_changelist")
            + "?"
            + urlencode({"test_name__id": f"{obj.id}"})
        )
        return format_html('<a href="{}"> Questions</a>', url)

    def get_queryset(self, request):
            qs = super().get_queryset(request)
            if request.user.is_superuser:
                return qs
            return qs.filter(user=request.user)

@admin.register(QuestionInstitute)
class QuestionInstituteAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                'question_number','question','a','b','c','d','correct_opt','correct_text'
            ),
           
        }),
         ("Scroll options",{
                'classes':('collapse',),
                'fields':('test_name',('category','subject'),('month','year'))
            }),
        ("True/False options",{
                'classes':('collapse',),
                'fields':(('comprehension_show','comprehension_doc'),('show','question_doc'),'doc')
            }),
        ("Comprehension and marks",{
            'classes':('collapse',),
            'fields':('comprehension',('correct_mark','negative_mark'))
        })
    )
    
    
    list_display = ['question_number','view_ids_link', 'question', 'test_name',
                    'category']
    search_fields = ['question', 'test_name', 'category']
    list_filter = ['year', 'subject', 'month', 'test_name', 'category']

    def view_ids_link(self, obj):

        url = (
        urlencode({"ssccgltestname__id": f"{obj.id}"})
        )
        return obj.id

    view_ids_link.short_description = "Id"

    def get_queryset(self, request):
            qs = super().get_queryset(request)
            if request.user.is_superuser:
                return qs
            return qs.filter(user=request.user)
            
# Bihar Police test name  models here


@admin.register(BiharPoliceTestName)
class Bihar_Police_TestNameAdmin(admin.ModelAdmin):
    list_display = ['test_name', 'category', 'view_question_link','view_ids_link']
    search_fields = ['test_name', 'category', 'keyword']
    list_filter = ['show_test', 'month', 'year',
                   'language',
                   'is_previous_year_question', 'category']


    def view_ids_link(self, obj):

        url = (
        urlencode({"biharpolicetestname__id": f"{obj.id}"})
        )
        return obj.id

    view_ids_link.short_description = "Id"

    def view_question_link(self, obj):

        url = (
            reverse("admin:mockapp_questionbiharpolice_changelist")
            + "?"
            + urlencode({"test_name__id": f"{obj.id}"})
        )
        return format_html('<a href="{}"> Questions</a>', url)

    view_question_link.short_description = "Questions"

    def get_queryset(self, request):
            qs = super().get_queryset(request)
            if request.user.is_superuser:
                return qs
            return qs.filter(user=request.user)

   

# RRB Test name models registered here


@admin.register(RRBNtpcTestName)
class RRB_NTPC_TestNameAdmin(admin.ModelAdmin):
    list_display = ['test_name', 'category', 'view_question_link','view_ids_link']
    search_fields = ['test_name', 'category', 'keyword']
    list_filter = ['show_test', 'month', 'year',
                   'language',
                   'is_previous_year_question', 'category']


    def view_ids_link(self, obj):

        url = (
        urlencode({"rrbntpctestname__id": f"{obj.id}"})
        )
        return obj.id

    view_ids_link.short_description = "Id"

    def view_question_link(self, obj):

        url = (
            reverse("admin:mockapp_questionrrbntpc_changelist")
            + "?"
            + urlencode({"test_name__id": f"{obj.id}"})
        )
        return format_html('<a href="{}"> Questions</a>', url)

    view_question_link.short_description = "Questions"

    def get_queryset(self, request):
            qs = super().get_queryset(request)
            if request.user.is_superuser:
                return qs
            return qs.filter(user=request.user)
   
@admin.register(RRBGroupDTestName)
class RRB_GROUPD_TestNameAdmin(admin.ModelAdmin):
    list_display = ['test_name', 'category', 'view_question_link','view_ids_link']
    search_fields = ['test_name', 'category', 'keyword']
    list_filter = ['show_test', 'language', 'month', 'year',
                   'is_previous_year_question', 'category']

    def view_ids_link(self, obj):

        url = (
        urlencode({"rrbgroupdtestname__id": f"{obj.id}"})
        )
        return obj.id

    view_ids_link.short_description = "Id"

    def view_question_link(self, obj):

        url = (
            reverse("admin:mockapp_questionrrbgroupd_changelist")
            + "?"
            + urlencode({"test_name__id": f"{obj.id}"})
        )
        return format_html('<a href="{}"> Questions</a>', url)

    view_question_link.short_description = "Questions"

    def get_queryset(self, request):
            qs = super().get_queryset(request)
            if request.user.is_superuser:
                return qs
            return qs.filter(user=request.user)
      
# Previous year RRB Test name models registered here


@admin.register(PreviousYearRRBGroupDTestName)
class PreviousYearRRB_GROUPD_TestNameAdmin(admin.ModelAdmin):
    list_display = ['test_name', 'category', 'view_question_link']
    search_fields = ['test_name', 'category', 'keyword']
    list_filter = ['show_test',
                   'language',
                   'month', 'year',
                   'is_previous_year_question', 'category']

    def view_question_link(self, obj):

        url = (
            reverse("admin:mockapp_previousyearquestionrrbgroupd_changelist")
            + "?"
            + urlencode({"test_name__id": f"{obj.id}"})
        )
        return format_html('<a href="{}"> Questions</a>', url)

    view_question_link.short_description = "Questions"


@admin.register(PreviousYearRRBNtpcTestName)
class PreviousYearRRB_NTPC_TestNameAdmin(admin.ModelAdmin):
    list_display = ['test_name', 'category']
    search_fields = ['test_name', 'category', 'keyword']
    list_filter = ['show_test',
                   # 'language',
                   'month', 'year',
                   'is_previous_year_question', 'category']


# SSC Test name models registered here


@admin.register(SSCCGLTestName)
class Ssc_Cgl_TestNameAdmin(admin.ModelAdmin):
    list_display = ['test_name', 'category', 'view_question_link','view_ids_link']
    search_fields = ['test_name', 'category', 'keyword']
    list_filter = ['show_test',
                   'language',
                   'month', 'year',
                   'is_previous_year_question', 'category']

    def view_ids_link(self, obj):

        url = (
        urlencode({"ssccgltestname__id": f"{obj.id}"})
        )
        return obj.id

    view_ids_link.short_description = "Id"

    def view_question_link(self, obj):

        url = (
            reverse("admin:mockapp_questionssccgl_changelist")
            + "?"
            + urlencode({"test_name__id": f"{obj.id}"})
        )
        return format_html('<a href="{}"> Questions</a>', url)

    view_question_link.short_description = "Questions"

    def get_queryset(self, request):
            qs = super().get_queryset(request)
            if request.user.is_superuser:
                return qs
            return qs.filter(user=request.user)
    

@admin.register(SSCCHSLTestName)
class Ssc_Chsl_TestNameAdmin(admin.ModelAdmin):
    list_display = ['test_name', 'category', 'view_question_link','view_ids_link']
    search_fields = ['test_name', 'category', 'keyword']
    list_filter = ['show_test',
                   'language',
                   'month', 'year',
                   'is_previous_year_question', 'category']

    def view_ids_link(self, obj):

        url = (
        urlencode({"sscchsltestname__id": f"{obj.id}"})
        )
        return obj.id

    view_ids_link.short_description = "Id"

    def view_question_link(self, obj):

        url = (
            reverse("admin:mockapp_questionsscchsl_changelist")
            + "?"
            + urlencode({"test_name__id": f"{obj.id}"})
        )
        return format_html('<a href="{}"> Questions</a>', url)

    view_question_link.short_description = "Questions"

    def get_queryset(self, request):
            qs = super().get_queryset(request)
            if request.user.is_superuser:
                return qs
            return qs.filter(user=request.user)
   

@admin.register(SSCJEEETestName)
class Ssc_Je_Ee_TestNameAdmin(admin.ModelAdmin):
    list_display = ['test_name', 'category','view_ids_link']
    search_fields = ['test_name', 'category', 'keyword']
    list_filter = ['show_test',
                   'language',
                   'month', 'year',
                   'is_previous_year_question', 'category']


    def view_ids_link(self, obj):

        url = (
        urlencode({"sscjeeetestname__id": f"{obj.id}"})
        )
        return obj.id

    view_ids_link.short_description = "Id"

    def get_queryset(self, request):
            qs = super().get_queryset(request)
            if request.user.is_superuser:
                return qs
            return qs.filter(user=request.user)


@admin.register(SscJeCeTestName)
class Ssc_Je_Ce_TestNameAdmin(admin.ModelAdmin):
    list_display = ['test_name', 'category','view_ids_link']
    search_fields = ['test_name', 'category', 'keyword']
    list_filter = ['show_test',
                   'language',
                   'month', 'year',
                   'is_previous_year_question', 'category']

    def view_ids_link(self, obj):

        url = (
        urlencode({"sscjecetestname__id": f"{obj.id}"})
        )
        return obj.id

    view_ids_link.short_description = "Id"

    def get_queryset(self, request):
            qs = super().get_queryset(request)
            if request.user.is_superuser:
                return qs
            return qs.filter(user=request.user)    
# Previous Year SSC TEST Name models registered here


@admin.register(PreviousYearSscJeCeTestName)
class PreviousYearSsc_Je_Ce_TestNameAdmin(admin.ModelAdmin):
    list_display = ['test_name', 'category']
    search_fields = ['test_name', 'category', 'keyword']
    list_filter = ['show_test',
                   'language',
                   'month', 'year',
                   'is_previous_year_question', 'category']


@admin.register(PreviousYearSSCJEEETestName)
class PreviousYearSsc_Je_Ee_TestNameAdmin(admin.ModelAdmin):
    list_display = ['test_name', 'category']
    search_fields = ['test_name', 'category', 'keyword']
    list_filter = ['show_test',
                   'language',
                   'month', 'year',
                   'is_previous_year_question', 'category']


@admin.register(PreviousYearSSCCHSLTestName)
class PreviousYearSsc_Chsl_TestNameAdmin(admin.ModelAdmin):
    list_display = ['test_name', 'category']
    search_fields = ['test_name', 'category', 'keyword']
    list_filter = ['show_test',
                   'language',
                   'month', 'year',
                   'is_previous_year_question', 'category']


@admin.register(PreviousYearSSCCGLTestName)
class PreviousYearSsc_Cgl_TestNameAdmin(admin.ModelAdmin):
    list_display = ['test_name', 'category']
    search_fields = ['test_name', 'category', 'keyword']
    list_filter = ['show_test',
                   'language',
                   'month', 'year',
                   'is_previous_year_question', 'category']

# Bihar Police questions models here


@admin.register(QuestionBiharPolice)
class Bihar_Police_QuestionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                'question_number','question','a','b','c','d','correct_opt','correct_text'
            ),
           
        }),
         ("Scroll options",{
                'classes':('collapse',),
                'fields':('test_name',('category','subject'),('month','year'))
            }),
        ("True/False options",{
                'classes':('collapse',),
                'fields':(('comprehension_show','comprehension_doc'),('show','question_doc'),'doc')
            }),
        ("Comprehension and marks",{
            'classes':('collapse',),
            'fields':('comprehension',('correct_mark','negative_mark'))
        })
    )
    
    
    list_display = ['question_number','view_ids_link', 'question', 'test_name',
                    'category']
    search_fields = ['question', 'test_name', 'category']
    list_filter = ['year', 'subject', 'month', 'test_name', 'category']

    def view_ids_link(self, obj):

        url = (
        urlencode({"ssccgltestname__id": f"{obj.id}"})
        )
        return obj.id

    view_ids_link.short_description = "Id"


    

# SSC question models registered here


@admin.register(QuestionSSCCGL)
class SSC_CGL_QuestionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
           "fields": (
                'question_number','question','a','b','c','d','correct_opt','correct_text'
            ),
        }),
        ("Scroll options",{
                'classes':('collapse',),
                'fields':('test_name',('category','subject'),('month','year'))
            }),
        ("True/False options",{
                'classes':('collapse',),
                'fields':(('comprehension_show','comprehension_doc'),('show','question_doc'),'doc')
            }),
        ("Comprehension and marks",{
            'classes':('collapse',),
            'fields':('comprehension',('correct_mark','negative_mark'))
        })
    )
    
    list_display = ['question_number', 'question', 'test_name',
                    'category']
    search_fields = ['question', 'test_name', 'category']
    list_filter = ['year', 'subject', 'month', 'test_name', 'category']

    def view_ids_link(self, obj):

        url = (
        urlencode({"ssccgltestname__id": f"{obj.id}"})
        )
        return obj.id

@admin.register(QuestionSSCCHSL)
class SSC_CHSL_QuestionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
           "fields": (
                'question_number','question','a','b','c','d','correct_opt','correct_text'
            ),
        }),
        ("Scroll options",{
                'classes':('collapse',),
                'fields':('test_name',('category','subject'),('month','year'))
            }),
        ("True/False options",{
                'classes':('collapse',),
                'fields':(('comprehension_show','comprehension_doc'),('show','question_doc'),'doc')
            }),
        ("Comprehension and marks",{
            'classes':('collapse',),
            'fields':('comprehension',('correct_mark','negative_mark'))
        })
    )
    
    list_display = ['question_number', 'question', 'test_name',
                    'category']
    search_fields = ['question', 'test_name', 'category']
    list_filter = ['year', 'subject', 'month', 'test_name', 'category']

    def view_ids_link(self, obj):

        url = (
        urlencode({"ssccgltestname__id": f"{obj.id}"})
        )
        return obj.id

@admin.register(QuestionSSCJEEE)
class SSC_JE_EE_QuestionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
           "fields": (
                'question_number','question','a','b','c','d','correct_opt','correct_text'
            ),
        }),
        ("Scroll options",{
                'classes':('collapse',),
                'fields':('test_name',('category','subject'),('month','year'))
            }),
        ("True/False options",{
                'classes':('collapse',),
                'fields':(('comprehension_show','comprehension_doc'),('show','question_doc'),'doc')
            }),
        ("Comprehension and marks",{
            'classes':('collapse',),
            'fields':('comprehension',('correct_mark','negative_mark'))
        })
    )
    
    list_display = ['question_number', 'question', 'test_name',
                    'category']
    search_fields = ['question', 'test_name', 'category']
    list_filter = ['year', 'subject', 'month', 'test_name', 'category']

    def view_ids_link(self, obj):

        url = (
        urlencode({"ssccgltestname__id": f"{obj.id}"})
        )
        return obj.id

@admin.register(QuestionSSCJECE)
class SSC_JE_CE_QuestionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
           "fields": (
                'question_number','question','a','b','c','d','correct_opt','correct_text'
            ),
        }),
        ("Scroll options",{
                'classes':('collapse',),
                'fields':('test_name',('category','subject'),('month','year'))
            }),
        ("True/False options",{
                'classes':('collapse',),
                'fields':(('comprehension_show','comprehension_doc'),('show','question_doc'),'doc')
            }),
        ("Comprehension and marks",{
            'classes':('collapse',),
            'fields':('comprehension',('correct_mark','negative_mark'))
        })
    )
    
    list_display = ['question_number', 'question', 'test_name',
                    'category']
    search_fields = ['question', 'test_name', 'category']
    list_filter = ['year', 'subject', 'month', 'test_name', 'category']

    def view_ids_link(self, obj):

        url = (
        urlencode({"ssccgltestname__id": f"{obj.id}"})
        )
        return obj.id
# Previous Year SSC Questions models registered here


@admin.register(PreviousYearQuestionSSCJECE)
class PreviousYearSSC_JE_CE_QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_number', 'question', 'test_name',
                    'category']
    search_fields = ['question', 'test_name', 'category']
    list_filter = ['year', 'subject', 'month', 'test_name', 'category']


@admin.register(PreviousYearQuestionSSCJEEE)
class PreviousYearSSC_JE_EE_QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_number', 'question', 'test_name',
                    'category']
    search_fields = ['question', 'test_name', 'category']
    list_filter = ['year', 'subject', 'month', 'test_name', 'category']


@admin.register(PreviousYearQuestionSSCCHSL)
class PreviousYearSSC_CHSL_QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_number', 'question', 'test_name',
                    'category']
    search_fields = ['question', 'test_name', 'category']
    list_filter = ['year', 'subject', 'month', 'test_name', 'category']


@admin.register(PreviousYearQuestionSSCCGL)
class PreviousYearSSC_CGL_QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_number', 'question', 'test_name',
                    'category']
    search_fields = ['question', 'test_name', 'category']
    list_filter = ['year', 'month', 'subject', 'test_name', 'category']


# RRB Question models registered here

@admin.register(QuestionRRBNtpc)
class RRB_NTPC_QuestionAdmin(admin.ModelAdmin):
    fieldsets = (
       (None, {
           "fields": (
                'question_number','question','a','b','c','d','correct_opt','correct_text'
            ),
        }),
        ("Scroll options",{
                'classes':('collapse',),
                'fields':('test_name',('category','subject'),('month','year'))
            }),
        ("True/False options",{
                'classes':('collapse',),
                'fields':(('comprehension_show','comprehension_doc'),('show','question_doc'),'doc')
            }),
        ("Comprehension and marks",{
            'classes':('collapse',),
            'fields':('comprehension',('correct_mark','negative_mark'))
        })
    )
    
    list_display = ['question_number', 'question', 'test_name',
                    'category']
    search_fields = ['question', 'test_name', 'category']
    list_filter = ['year', 'subject', 'month', 'test_name', 'category']
    change_links = ['test_name']

    def view_ids_link(self, obj):

        url = (
        urlencode({"ssccgltestname__id": f"{obj.id}"})
        )
        return obj.id

@admin.register(QuestionRRBGroupD)
class RRB_GROUPD_QuestionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
           "fields": (
                'question_number','question','a','b','c','d','correct_opt','correct_text'
            ),
        }),
        ("Scroll options",{
                'classes':('collapse',),
                'fields':('test_name',('category','subject'),('month','year'))
            }),
        ("True/False options",{
                'classes':('collapse',),
                'fields':(('comprehension_show','comprehension_doc'),('show','question_doc'),'doc')
            }),
        ("Comprehension and marks",{
            'classes':('collapse',),
            'fields':('comprehension',('correct_mark','negative_mark'))
        })
    )
    
    list_display = ['question_number', 'question', 'test_name',
                    'category']
    search_fields = ['question', 'test_name', 'category']
    list_filter = ['year', 'subject', 'month', 'test_name', 'category']

    def view_ids_link(self, obj):

        url = (
        urlencode({"ssccgltestname__id": f"{obj.id}"})
        )
        return obj.id
# Previous Year RRB Question models registered here


@admin.register(PreviousYearQuestionRRBNtpc)
class PreviousYearRRB_NTPC_QuestionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                
            ),
        }),
    )
    
    list_display = ['question_number', 'question', 'test_name',
                    'category']
    search_fields = ['question', 'test_name', 'category']
    list_filter = ['year', 'subject', 'month', 'test_name', 'category']


@admin.register(PreviousYearQuestionRRBGroupD)
class PreviousYearRRB_GROUPD_QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_number', 'question', 'test_name',
                    'category']
    search_fields = ['question', 'test_name', 'category']
    list_filter = ['year', 'subject', 'month', 'test_name', 'category']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_number', 'question', 'test_name',
                    'category']
    search_fields = ['question', 'test_name', 'category']
    list_filter = ['year', 'month', 'test_name', 'category']
