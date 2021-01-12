from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(LanguageSelector)
class LanguageAdmin(admin.ModelAdmin):
    list_display=['lang_name','lang_no']

@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display=['policy_no','policy_title']
    list_filter=['policy_no','show']

@admin.register(FAQ)
class FaqAdmin(admin.ModelAdmin):
    list_display=['faq_no','faq_question']
    list_filter=['faq_no','show']

@admin.register(FAQSSCChsl)
class FaqSSCAdmin(admin.ModelAdmin):
    list_display=['faq_no','faq_question']
    list_filter=['faq_no','show']

@admin.register(TermsCondition)
class TermsConditionAdmin(admin.ModelAdmin):
    list_display=['term_no','term_title']
    list_filter=['term_no','show']    

@admin.register(PreviousYear)
class PreviousYearAdmin(admin.ModelAdmin):
    list_display = ['year']


@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ['year']


@admin.register(Month)
class MonthAdmin(admin.ModelAdmin):
    list_display = ['month']


@admin.register(TestCategory)
class TestCategoryAdmin(admin.ModelAdmin):
    list_display = ['category']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject']


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


# RRB Test name models registered here


@admin.register(RRBNtpcTestName)
class RRB_NTPC_TestNameAdmin(admin.ModelAdmin):
    list_display = ['test_name', 'category']
    search_fields = ['test_name', 'category', 'keyword']
    list_filter = ['show_test', 'month', 'year',
                  'language',
                   'is_previous_year_question', 'category']


@admin.register(RRBGroupDTestName)
class RRB_GROUPD_TestNameAdmin(admin.ModelAdmin):
    list_display = ['test_name', 'category']
    search_fields = ['test_name', 'category', 'keyword']
    list_filter = ['show_test'
                    ,'language'
                   , 'month', 'year',
                   'is_previous_year_question', 'category']

# Previous year RRB Test name models registered here


@admin.register(PreviousYearRRBGroupDTestName)
class PreviousYearRRB_GROUPD_TestNameAdmin(admin.ModelAdmin):
    list_display = ['test_name', 'category']
    search_fields = ['test_name', 'category', 'keyword']
    list_filter = ['show_test',
                  'language', 
                  'month', 'year',
                   'is_previous_year_question', 'category']


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
    list_display = ['test_name', 'category']
    search_fields = ['test_name', 'category', 'keyword']
    list_filter = ['show_test',
                    'language',
                     'month', 'year',
                   'is_previous_year_question', 'category']


@admin.register(SSCCHSLTestName)
class Ssc_Chsl_TestNameAdmin(admin.ModelAdmin):
    list_display = ['test_name', 'category']
    search_fields = ['test_name', 'category', 'keyword']
    list_filter = ['show_test',
                    'language',
                     'month', 'year',
                   'is_previous_year_question', 'category']


@admin.register(SSCJEEETestName)
class Ssc_Je_Ee_TestNameAdmin(admin.ModelAdmin):
    list_display = ['test_name', 'category']
    search_fields = ['test_name', 'category', 'keyword']
    list_filter = ['show_test',
                    'language',
                     'month', 'year',
                   'is_previous_year_question', 'category']


@admin.register(SscJeCeTestName)
class Ssc_Je_Ce_TestNameAdmin(admin.ModelAdmin):
    list_display = ['test_name', 'category']
    search_fields = ['test_name', 'category', 'keyword']
    list_filter = ['show_test',
                    'language',
                    'month', 'year',
                   'is_previous_year_question', 'category']

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

# SSC question models registered here


@admin.register(QuestionSSCCGL)
class SSC_CGL_QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_number','question', 'test_name',
                    'category'  ]
    search_fields = ['question', 'test_name', 'category']
    list_filter = ['year','subject', 'month', 'test_name', 'category']


@admin.register(QuestionSSCCHSL)
class SSC_CHSL_QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_number','question', 'test_name',
                    'category'  ]
    search_fields = ['question', 'test_name', 'category']
    list_filter = ['year', 'subject','month', 'test_name', 'category']


@admin.register(QuestionSSCJEEE)
class SSC_JE_EE_QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_number','question', 'test_name',
                    'category' ]
    search_fields = ['question', 'test_name', 'category']
    list_filter = ['year','subject', 'month', 'test_name', 'category']


@admin.register(QuestionSSCJECE)
class SSC_JE_CE_QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_number','question', 'test_name',
                    'category']
    search_fields = ['question', 'test_name', 'category']
    list_filter = ['year','subject', 'month', 'test_name', 'category']

# Previous Year SSC Questions models registered here


@admin.register(PreviousYearQuestionSSCJECE)
class PreviousYearSSC_JE_CE_QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_number','question', 'test_name',
                    'category']
    search_fields = ['question', 'test_name', 'category']
    list_filter = ['year','subject', 'month', 'test_name', 'category']


@admin.register(PreviousYearQuestionSSCJEEE)
class PreviousYearSSC_JE_EE_QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_number','question', 'test_name',
                    'category' ]
    search_fields = ['question', 'test_name', 'category']
    list_filter = ['year','subject', 'month', 'test_name', 'category']


@admin.register(PreviousYearQuestionSSCCHSL)
class PreviousYearSSC_CHSL_QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_number','question', 'test_name',
                    'category' ]
    search_fields = ['question', 'test_name', 'category']
    list_filter = ['year','subject', 'month', 'test_name', 'category']


@admin.register(PreviousYearQuestionSSCCGL)
class PreviousYearSSC_CGL_QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_number','question', 'test_name',
                    'category']
    search_fields = ['question', 'test_name', 'category']
    list_filter = ['year', 'month','subject', 'test_name', 'category']


# RRB Question models registered here

@admin.register(QuestionRRBNtpc)
class RRB_NTPC_QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_number','question', 'test_name',
                    'category']
    search_fields = ['question', 'test_name', 'category']
    list_filter = ['year','subject', 'month', 'test_name', 'category']


@admin.register(QuestionRRBGroupD)
class RRB_GROUPD_QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_number','question', 'test_name',
                    'category' ]
    search_fields = ['question', 'test_name', 'category']
    list_filter = ['year','subject', 'month', 'test_name', 'category']

# Previous Year RRB Question models registered here


@admin.register(PreviousYearQuestionRRBNtpc)
class PreviousYearRRB_NTPC_QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_number','question', 'test_name',
                    'category' ]
    search_fields = ['question', 'test_name', 'category']
    list_filter = ['year','subject', 'month', 'test_name', 'category']


@admin.register(PreviousYearQuestionRRBGroupD)
class PreviousYearRRB_GROUPD_QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_number','question', 'test_name',
                    'category' ]
    search_fields = ['question', 'test_name', 'category']
    list_filter = ['year','subject', 'month', 'test_name', 'category']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_number','question', 'test_name',
                    'category' ]
    search_fields = ['question', 'test_name', 'category']
    list_filter = ['year', 'month', 'test_name', 'category']
    
