from rest_framework import serializers
from .models import *


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageSelector
        fields = ['id', 'lang_no', 'lang_name', 'show']


class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = ['id', 'year', 'pub_date', 'edit_date']

# privacy policy model serializers


class PrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = ['id', 'policy_no', 'policy_title',
                  'policy_description', 'show']


# FAQ model serializer
class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'faq_no', 'faq_question', 'faq_answer', 'show']

# Terms & Conditions serializers


class TermsConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermsCondition
        fields = ['id', 'term_no', 'term_title', 'term_desc', 'show']

# Previous Year model serializer


class PreviousYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreviousYear
        fields = ['id', 'year', 'pub_date', 'edit_date']


class MonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Month
        fields = ['id', 'month', 'pub_date', 'edit_date']


class TestCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCategory
        fields = ['id', 'category', 'pub_date', 'edit_date', 'keyword', 'preview_keyword',
                  'previous_year_keyword', 'preview_previous_year_keyword', 'show',
                  'preview_show']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'subject', 'pub_date', 'edit_date']


class TestNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestName
        fields = ['id', 'month', 'year', 'test_name', 'test_time',
                  'category', 'keyword']

# Article info and points serializers


class ArticleInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleInfo
        fields = [
            'id', 'title', 'category', 'pub_date', 'short_description', 'cat_text', 'month', 'year', 'image', 'info_no', 'keyword', 'show'
        ]


class ArticleInfoPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleInfoPoints
        fields = ['id', 'point_no', 'job_info', 'title',
                  'description', 'show', 'image_show', 'image_url']


# Job info and point serilizers
class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = ['id', 'category', 'pub_date', 'edit_date', 'keyword', 'preview_keyword',
                  'previous_year_keyword', 'preview_previous_year_keyword', 'show',
                  'preview_show']

class JobInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobInfo
        fields = [
            'id', 'title', 'category', 'category_job','pub_date', 'short_description', 'cat_text', 'month', 'year', 'image', 'info_no', 'keyword', 'show'
        ]


class JobInfoPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobInfoPoints
        fields = ['id', 'point_no', 'job_info', 'title',
                  'description', 'show', 'image_show', 'image_url']

# Bihar police test name serializer


class Bihar_Police_TestNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiharPoliceTestName
        fields = ['id', 'test_number', 'month', 'year', 'test_name', 'test_time', 'show_test',
                  'is_previous_year_question',
                  'total_no_of_question',
                  'language',
                  'category', 'keyword']

# RRB Test name serializers here


class RRB_NTPC_TestNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = RRBNtpcTestName
        fields = ['id', 'test_number', 'month', 'year', 'test_name', 'test_time', 'show_test',
                  'is_previous_year_question',
                  'total_no_of_question',
                  'language',
                  'category', 'keyword']


class RRB_GROUPD_TestNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = RRBGroupDTestName
        fields = ['id', 'test_number', 'month', 'year', 'test_name', 'test_time', 'show_test',
                  'is_previous_year_question',
                  'total_no_of_question',
                  'language',
                  'category', 'keyword']

# Previous Year RRB Test Names serializers here


class PreviousYearRRB_NTPC_TestNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreviousYearRRBNtpcTestName
        fields = ['id', 'test_number', 'month', 'year', 'test_name', 'test_time', 'show_test',
                  'is_previous_year_question',
                  'total_no_of_question',
                  'language',
                  'category', 'keyword']


class PreviousYearRRB_GROUPD_TestNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreviousYearRRBGroupDTestName
        fields = ['id', 'test_number', 'month', 'year', 'test_name', 'test_time', 'show_test',
                  'is_previous_year_question',
                  'total_no_of_question',
                  'language',
                  'category', 'keyword']


# SSC test name serializers here

class SSC_CGL_TestNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSCCGLTestName
        fields = ['id', 'test_number', 'month', 'year', 'test_name', 'test_time', 'show_test',
                  'is_previous_year_question',
                  'total_no_of_question',
                  'language',
                  'category', 'keyword']


class SSC_CHSL_TestNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSCCHSLTestName
        fields = ['id', 'test_number', 'month', 'year', 'test_name', 'test_time', 'show_test',
                  'is_previous_year_question',
                  'total_no_of_question',
                  'language',
                  'category', 'keyword']


class SSC_JE_EE_TestNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSCJEEETestName
        fields = ['id', 'test_number', 'month', 'year', 'test_name', 'test_time', 'show_test',
                  'is_previous_year_question',
                  'total_no_of_question',
                  'language',
                  'category', 'keyword']


class SSC_JE_CE_TestNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = SscJeCeTestName
        fields = ['id', 'test_number', 'month', 'year', 'test_name', 'test_time', 'show_test',
                  'is_previous_year_question',
                  'total_no_of_question',
                  'language',
                  'category', 'keyword']

# Previous Year SSC Test Names here


class PreviousYearSSC_CGL_TestNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreviousYearSSCCGLTestName
        fields = ['id', 'test_number', 'month', 'year', 'test_name', 'test_time', 'show_test',
                  'is_previous_year_question',
                  'total_no_of_question',
                  'language',
                  'category', 'keyword']


class PreviousYearSSC_CHSL_TestNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreviousYearSSCCHSLTestName
        fields = ['id', 'test_number', 'month', 'year', 'test_name', 'test_time', 'show_test',
                  'is_previous_year_question',
                  'total_no_of_question',
                  'language',
                  'category', 'keyword']


class PreviousYearSSC_JE_EE_TestNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreviousYearSSCJEEETestName
        fields = ['id', 'test_number', 'month', 'year', 'test_name', 'test_time', 'show_test',
                  'is_previous_year_question',
                  'total_no_of_question',
                  'language',
                  'category', 'keyword']


class PreviousYearSSC_JE_CE_TestNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreviousYearSscJeCeTestName
        fields = ['id', 'test_number', 'month', 'year', 'test_name', 'test_time', 'show_test',
                  'is_previous_year_question',
                  'total_no_of_question',
                  'language',
                  'category', 'keyword']

# Bihar Police question serializer


class Bihar_Police_QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionBiharPolice
        fields = ['id',  'test_name', 'category', 'subject', 'month',
                  'comprehension_show', 'comprehension_doc', 'question_doc', 'doc', 'comprehension',
                  'year', 'show', 'question', 'a', 'b', 'c', 'd', 'correct_opt', 'question_number',
                  'correct_mark', 'correct_text', 'negative_mark']


# RRB Question serializers


class RRB_NTPC_QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionRRBNtpc
        fields = ['id',  'test_name', 'category', 'subject', 'month',
                  'comprehension_show', 'comprehension_doc', 'question_doc', 'doc', 'comprehension',
                  'year', 'show', 'question', 'a', 'b', 'c', 'd', 'correct_opt', 'question_number',
                  'correct_mark', 'correct_text', 'negative_mark']


class RRB_GROUPD_QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionRRBGroupD
        fields = ['id',  'test_name', 'category', 'subject', 'month',
                  'comprehension_show', 'comprehension_doc', 'question_doc', 'doc', 'comprehension',
                  'year', 'show', 'question', 'a', 'b', 'c', 'd', 'correct_opt',
                  'question_number', 'correct_mark', 'correct_text', 'negative_mark']

# RRB Previous Year serializers here


class PreviousYearRRB_NTPC_QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreviousYearQuestionRRBNtpc
        fields = ['id',  'test_name', 'category', 'subject', 'month',
                  'comprehension_show', 'comprehension_doc', 'question_doc', 'doc', 'comprehension',
                  'year', 'show', 'question', 'a', 'b', 'c', 'd', 'correct_opt',
                  'question_number', 'correct_mark', 'correct_text', 'negative_mark']


class PreviousYearRRB_GROUPD_QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreviousYearQuestionRRBGroupD
        fields = ['id',  'test_name', 'category', 'subject', 'month',
                  'comprehension_show', 'comprehension_doc', 'question_doc', 'doc', 'comprehension',
                  'year', 'show', 'question', 'a', 'b', 'c', 'd', 'correct_opt',
                  'question_number', 'correct_mark', 'correct_text', 'negative_mark']

 # SSC Questions serializers here


class SSC_CGL_QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionSSCCGL
        fields = ['id',  'test_name', 'category', 'subject', 'month',
                  'comprehension_show', 'comprehension_doc', 'question_doc', 'doc', 'comprehension',
                  'year', 'show', 'question', 'a', 'b', 'c', 'd', 'correct_opt',
                  'question_number', 'correct_mark', 'correct_text', 'negative_mark']


class SSC_CHSL_QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionSSCCHSL
        fields = ['id',  'test_name', 'category', 'subject', 'month',
                  'comprehension_show', 'comprehension_doc', 'question_doc', 'doc', 'comprehension',
                  'year', 'show', 'question', 'a', 'b', 'c', 'd', 'correct_opt',
                  'question_number', 'correct_mark', 'correct_text', 'negative_mark']


class SSC_JE_EE_QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionSSCJEEE
        fields = ['id',  'test_name', 'category', 'subject', 'month',
                  'comprehension_show', 'comprehension_doc', 'question_doc', 'doc', 'comprehension',
                  'year', 'show', 'question', 'a', 'b', 'c', 'd', 'correct_opt',
                  'question_number', 'correct_mark', 'correct_text', 'negative_mark']


class SSC_JE_CE_QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionSSCJECE
        fields = ['id',  'test_name', 'category', 'subject', 'month',
                  'comprehension_show', 'comprehension_doc', 'question_doc', 'doc', 'comprehension',
                  'year', 'show', 'question', 'a', 'b', 'c', 'd', 'correct_opt',
                  'question_number', 'correct_mark', 'correct_text', 'negative_mark']

# Previous Year SSC Question Serializer


class PreviousYearSSC_CGL_QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreviousYearQuestionSSCCGL
        fields = ['id',  'test_name', 'category', 'subject', 'month',
                  'comprehension_show', 'comprehension_doc', 'question_doc', 'doc', 'comprehension',
                  'year', 'show', 'question', 'a', 'b', 'c', 'd', 'correct_opt',
                  'question_number', 'correct_mark', 'correct_text', 'negative_mark']


class PreviousYearSSC_CHSL_QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreviousYearQuestionSSCCHSL
        fields = ['id',  'test_name', 'category', 'subject', 'month',
                  'comprehension_show', 'comprehension_doc', 'question_doc', 'doc', 'comprehension',
                  'year', 'show', 'question', 'a', 'b', 'c', 'd', 'correct_opt',
                  'question_number', 'correct_mark', 'correct_text', 'negative_mark']


class PreviousYearSSC_JE_EE_QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreviousYearQuestionSSCJEEE
        fields = ['id',  'test_name', 'category', 'subject', 'month',
                  'comprehension_show', 'comprehension_doc', 'question_doc', 'doc', 'comprehension',
                  'year', 'show', 'question', 'a', 'b', 'c', 'd', 'correct_opt',
                  'question_number', 'correct_mark', 'correct_text', 'negative_mark']


class PreviousYearSSC_JE_CE_QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreviousYearQuestionSSCJECE
        fields = ['id',  'test_name', 'category', 'subject', 'month',
                  'comprehension_show', 'comprehension_doc', 'question_doc', 'doc', 'comprehension',
                  'year', 'show', 'question', 'a', 'b', 'c', 'd', 'correct_opt',
                  'question_number', 'correct_mark', 'correct_text', 'negative_mark']

# Question model serializer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id',  'test_name', 'category', 'subject', 'month',
                  'comprehension_show', 'comprehension_doc', 'question_doc', 'doc', 'comprehension',
                  'year', 'show', 'question', 'a', 'b', 'c', 'd', 'correct_opt', 'question_number']
