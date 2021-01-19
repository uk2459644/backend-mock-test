from django.shortcuts import render
from .models import *
from .serializers import *
from django.http import HttpResponse, JsonResponse

# Create your views here.

# getting language list 
def get_language_list(request):
      if  request.method == 'GET':
        lang_list=LanguageSelector.objects.filter(show=True).order_by('lang_no')
        serializer=LanguageSerializer(lang_list,many=True)
        return JsonResponse(serializer.data,safe=False)

# getting privacy policy , faq and terms data
def privacy_policy_list(request):
    if request.method == 'GET':
        policy_list=PrivacyPolicy.objects.filter(show=True).order_by('policy_no')
        serializer=PrivacyPolicySerializer(policy_list,many=True)
        return JsonResponse(serializer.data,safe=False)

def faq_list(request):
    if request.method == 'GET':
        policy_list=FAQ.objects.filter(show=True).order_by('faq_no')
        serializer=FAQSerializer(policy_list,many=True)
        return JsonResponse(serializer.data,safe=False)


def terms_list(request):
    if request.method == 'GET':
        policy_list=TermsCondition.objects.filter(show=True).order_by('term_no')
        serializer=TermsConditionSerializer(policy_list,many=True)
        return JsonResponse(serializer.data,safe=False)

# getting list of categories
def get_categories_list(request):
    if request.method == 'GET':
        catlist=TestCategory.objects.filter(show=True)
        serializer=TestCategorySerializer(catlist,many=True)
        return JsonResponse(serializer.data,safe=False)

def preview_get_categories_list(request):
    if request.method == 'GET':
        catlist=TestCategory.objects.filter(preview_show=True)
        serializer=TestCategorySerializer(catlist,many=True)
        return JsonResponse(serializer.data,safe=False)


#  getting bihar police test names and questions
def bihar_police_testlist(request):

    if request.method == 'GET':
        testlist = BiharPoliceTestName.objects.filter(
            is_previous_year_question=False,show_test=True).order_by('test_number')
        serializer = Bihar_Police_TestNameSerializer(testlist, many=True)
        return JsonResponse(serializer.data, safe=False)

def preview_bihar_police_testlist(request):

    if request.method == 'GET':
        testlist = BiharPoliceTestName.objects.filter(
            is_previous_year_question=False,show_test=False).order_by('test_number')
        serializer = Bihar_Police_TestNameSerializer(testlist, many=True)
        return JsonResponse(serializer.data, safe=False)
         
def bihar_police_questions_by_test_name(request, cid):
    if request.method == 'GET':
        questionlist = QuestionBiharPolice.objects.filter(
            test_name=cid).order_by('question_number')
        serializer = Bihar_Police_QuestionSerializer(questionlist, many=True)
        return JsonResponse(serializer.data, safe=False)

# getting ssc cgl test name and questions list ordered by test number


def ssc_cgl_testlist(request):

    if request.method == 'GET':
        testlist = SSCCGLTestName.objects.filter(
            is_previous_year_question=False,show_test=True).order_by('test_number')
        serializer = SSC_CGL_TestNameSerializer(testlist, many=True)
        return JsonResponse(serializer.data, safe=False)

def preview_ssc_cgl_testlist(request):

    if request.method == 'GET':
        testlist = SSCCGLTestName.objects.filter(
            is_previous_year_question=False,show_test=False).order_by('test_number')
        serializer = SSC_CGL_TestNameSerializer(testlist, many=True)
        return JsonResponse(serializer.data, safe=False)

def ssc_cgl_testlist_previous_year(request):

    if request.method == 'GET':
        testlist = PreviousYearSSCCGLTestName.objects.filter(
            is_previous_year_question=True,show_test=True).order_by('test_number')
        serializer = PreviousYearSSC_CGL_TestNameSerializer(testlist, many=True)
        return JsonResponse(serializer.data, safe=False)

def preview_ssc_cgl_testlist_previous_year(request):

    if request.method == 'GET':
        testlist = PreviousYearSSCCGLTestName.objects.filter(
            is_previous_year_question=True,show_test=False).order_by('test_number')
        serializer = PreviousYearSSC_CGL_TestNameSerializer(testlist, many=True)
        return JsonResponse(serializer.data, safe=False)


def ssc_cgl_questions_by_test_name(request, cid):
    if request.method == 'GET':
        questionlist = QuestionSSCCGL.objects.filter(
            test_name=cid).order_by('question_number')
        serializer = SSC_CGL_QuestionSerializer(questionlist, many=True)
        return JsonResponse(serializer.data, safe=False)

def previous_year_ssc_cgl_questions_by_test_name(request, cid):
    if request.method == 'GET':
        questionlist = PreviousYearQuestionSSCCGL.objects.filter(
            test_name=cid).order_by('question_number')
        serializer = PreviousYearSSC_CGL_QuestionSerializer(questionlist, many=True)
        return JsonResponse(serializer.data, safe=False)


# getting ssc chsl test name and questions list ordered by test number


def ssc_chsl_testlist(request):

    if request.method == 'GET':
        testlist = SSCCHSLTestName.objects.filter(
            is_previous_year_question=False,show_test=True).order_by('test_number')
        serializer = SSC_CHSL_TestNameSerializer(testlist, many=True)
        return JsonResponse(serializer.data, safe=False)

def preview_ssc_chsl_testlist(request):

    if request.method == 'GET':
        testlist = SSCCHSLTestName.objects.filter(
            is_previous_year_question=False,show_test=False).order_by('test_number')
        serializer = SSC_CHSL_TestNameSerializer(testlist, many=True)
        return JsonResponse(serializer.data, safe=False)

def ssc_chsl_testlist_previous_year(request):

    if request.method == 'GET':
        testlist = PreviousYearSSCCHSLTestName.objects.filter(
            is_previous_year_question=True,show_test=True).order_by('test_number')
        serializer =PreviousYearSSC_CHSL_TestNameSerializer(testlist, many=True)
        return JsonResponse(serializer.data, safe=False)

def preview_ssc_chsl_testlist_previous_year(request):

    if request.method == 'GET':
        testlist = PreviousYearSSCCHSLTestName.objects.filter(
            is_previous_year_question=True,show_test=False).order_by('test_number')
        serializer =PreviousYearSSC_CHSL_TestNameSerializer(testlist, many=True)
        return JsonResponse(serializer.data, safe=False)

def ssc_chsl_questions_by_test_name(request, cid):
    if request.method == 'GET':
        questionlist = QuestionSSCCHSL.objects.filter(
            test_name=cid).order_by('question_number')
        serializer = SSC_CHSL_QuestionSerializer(questionlist, many=True)
        return JsonResponse(serializer.data, safe=False)

def previous_year_ssc_chsl_questions_by_test_name(request, cid):
    if request.method == 'GET':
        questionlist =PreviousYearQuestionSSCCHSL.objects.filter(
            test_name=cid).order_by('question_number')
        serializer = PreviousYearSSC_CHSL_QuestionSerializer(questionlist, many=True)
        return JsonResponse(serializer.data, safe=False)

# getting ssc je-ee test name and questions list ordered by test number


def ssc_je_ee_testlist(request):

    if request.method == 'GET':
        testlist = SSCJEEETestName.objects.filter(
            is_previous_year_question=False,show_test=True).order_by('test_number')
        serializer = SSC_JE_EE_TestNameSerializer(testlist, many=True)
        return JsonResponse(serializer.data, safe=False)

def preview_ssc_je_ee_testlist(request):

    if request.method == 'GET':
        testlist = SSCJEEETestName.objects.filter(
            is_previous_year_question=False,show_test=False).order_by('test_number')
        serializer = SSC_JE_EE_TestNameSerializer(testlist, many=True)
        return JsonResponse(serializer.data, safe=False)

def ssc_je_ee_testlist_previous_year(request):

    if request.method == 'GET':
        testlist = PreviousYearSSCJEEETestName.objects.filter(
            is_previous_year_question=True,show_test=True).order_by('test_number')
        serializer = PreviousYearSSC_JE_EE_TestNameSerializer(testlist, many=True)
        return JsonResponse(serializer.data, safe=False)

def preview_ssc_je_ee_testlist_previous_year(request):

    if request.method == 'GET':
        testlist = PreviousYearSSCJEEETestName.objects.filter(
            is_previous_year_question=True,show_test=False).order_by('test_number')
        serializer = PreviousYearSSC_JE_EE_TestNameSerializer(testlist, many=True)
        return JsonResponse(serializer.data, safe=False)


def ssc_je_ee_questions_by_test_name(request, cid):
    if request.method == 'GET':
        questionlist = QuestionSSCJEEE.objects.filter(
            test_name=cid).order_by('question_number')
        serializer = SSC_JE_EE_QuestionSerializer(questionlist, many=True)
        return JsonResponse(serializer.data, safe=False)

def previous_year_ssc_je_ee_questions_by_test_name(request, cid):
    if request.method == 'GET':
        questionlist = PreviousYearQuestionSSCJEEE.objects.filter(
            test_name=cid).order_by('question_number')
        serializer = PreviousYearSSC_JE_EE_QuestionSerializer(questionlist, many=True)
        return JsonResponse(serializer.data, safe=False)

# getting ssc je ce test name and questions  list ordered by test number


def ssc_je_ce_testlist(request):

    if request.method == 'GET':
        testlist = SscJeCeTestName.objects.filter(
            is_previous_year_question=False,show_test=True).order_by('test_number')
        serializer = SSC_JE_CE_TestNameSerializer(testlist, many=True)
        return JsonResponse(serializer.data, safe=False)

def preview_ssc_je_ce_testlist(request):

    if request.method == 'GET':
        testlist = SscJeCeTestName.objects.filter(
            is_previous_year_question=False,show_test=False).order_by('test_number')
        serializer = SSC_JE_CE_TestNameSerializer(testlist, many=True)
        return JsonResponse(serializer.data, safe=False)

def ssc_je_ce_testlist_previous_year(request):

    if request.method == 'GET':
        testlist = PreviousYearSscJeCeTestName.objects.filter(
            is_previous_year_question=True,show_test=True).order_by('test_number')
        serializer = PreviousYearSSC_JE_CE_TestNameSerializer(testlist, many=True)
        return JsonResponse(serializer.data, safe=False)

def preview_ssc_je_ce_testlist_previous_year(request):

    if request.method == 'GET':
        testlist = PreviousYearSscJeCeTestName.objects.filter(
            is_previous_year_question=True,show_test=False).order_by('test_number')
        serializer = PreviousYearSSC_JE_CE_TestNameSerializer(testlist, many=True)
        return JsonResponse(serializer.data, safe=False)


def ssc_je_ce_questions_by_test_name(request, cid):
    if request.method == 'GET':
        questionlist = QuestionSSCJECE.objects.filter(
            test_name=cid).order_by('question_number')
        serializer = SSC_JE_CE_QuestionSerializer(questionlist, many=True)
        return JsonResponse(serializer.data, safe=False)

def previous_year_ssc_je_ce_questions_by_test_name(request, cid):
    if request.method == 'GET':
        questionlist = PreviousYearQuestionSSCJECE.objects.filter(
            test_name=cid).order_by('question_number')
        serializer = PreviousYearSSC_JE_CE_QuestionSerializer(questionlist, many=True)
        return JsonResponse(serializer.data, safe=False)

# getting rrb ntpc test name and questions list ordered by test number
def rrb_ntpc_testlist(request):

    if request.method == 'GET':
        testlist = RRBNtpcTestName.objects.filter(
            is_previous_year_question=False,show_test=True).order_by('test_number')
        serializer = RRB_NTPC_TestNameSerializer(testlist, many=True)

        return JsonResponse(serializer.data, safe=False)

def preview_rrb_ntpc_testlist(request):

    if request.method == 'GET':
        testlist = RRBNtpcTestName.objects.filter(
            is_previous_year_question=False,show_test=False).order_by('test_number')
        serializer = RRB_NTPC_TestNameSerializer(testlist, many=True)

        return JsonResponse(serializer.data, safe=False)

def rrb_ntpc_testlist_previous_year(request):

    if request.method == 'GET':
        testlist = PreviousYearRRBNtpcTestName.objects.filter(
            is_previous_year_question=True,show_test=True).order_by('test_number')
        serializer = PreviousYearRRB_NTPC_TestNameSerializer(testlist, many=True)

        return JsonResponse(serializer.data, safe=False)

def preview_rrb_ntpc_testlist_previous_year(request):

    if request.method == 'GET':
        testlist = PreviousYearRRBNtpcTestName.objects.filter(
            is_previous_year_question=True,show_test=False).order_by('test_number')
        serializer = PreviousYearRRB_NTPC_TestNameSerializer(testlist, many=True)

        return JsonResponse(serializer.data, safe=False)

def rrb_ntpc_questions_by_test_name(request, cid):

    if request.method == 'GET':
        questionlist = QuestionRRBNtpc.objects.filter(
            test_name=cid).order_by('question_number')
        serializer = RRB_NTPC_QuestionSerializer(questionlist, many=True)

        return JsonResponse(serializer.data, safe=False)

def previous_year_rrb_ntpc_questions_by_test_name(request, cid):

    if request.method == 'GET':
        questionlist = PreviousYearQuestionRRBNtpc.objects.filter(
            test_name=cid).order_by('question_number')
        serializer = PreviousYearRRB_NTPC_QuestionSerializer(questionlist, many=True)

        return JsonResponse(serializer.data, safe=False)

# getting rrb group d test name and questions list ordered by test number
def rrb_groupd_testlist(request):

    if request.method == 'GET':
        testlist = RRBGroupDTestName.objects.filter(
            is_previous_year_question=False,show_test=True).order_by('test_number')
        serializer = RRB_GROUPD_TestNameSerializer(testlist, many=True)
        return JsonResponse(serializer.data, safe=False)

def preview_rrb_groupd_testlist(request):

    if request.method == 'GET':
        testlist = RRBGroupDTestName.objects.filter(
            is_previous_year_question=False,show_test=False).order_by('test_number')
        serializer = RRB_GROUPD_TestNameSerializer(testlist, many=True)
        return JsonResponse(serializer.data, safe=False)

def rrb_groupd_testlist_previous_year(request):

    if request.method == 'GET':
        testlist = PreviousYearRRBGroupDTestName.objects.filter(
            is_previous_year_question=True,show_test=True).order_by('test_number')
        serializer = PreviousYearRRB_GROUPD_TestNameSerializer(testlist, many=True)
        return JsonResponse(serializer.data, safe=False)

def preview_rrb_groupd_testlist_previous_year(request):

    if request.method == 'GET':
        testlist = PreviousYearRRBGroupDTestName.objects.filter(
            is_previous_year_question=True,show_test=False).order_by('test_number')
        serializer = PreviousYearRRB_GROUPD_TestNameSerializer(testlist, many=True)
        return JsonResponse(serializer.data, safe=False)

def rrb_groupd_questions_by_test_name(request, cid):
    if request.method == 'GET':
        questionlist = QuestionRRBGroupD.objects.filter(
            test_name=cid).order_by('question_number')
        serializer = RRB_GROUPD_QuestionSerializer(questionlist, many=True)

        return JsonResponse(serializer.data, safe=False)

def previous_year_rrb_groupd_questions_by_test_name(request, cid):
    if request.method == 'GET':
        questionlist = PreviousYearQuestionRRBGroupD.objects.filter(
            test_name=cid).order_by('question_number')
        serializer = PreviousYearRRB_GROUPD_QuestionSerializer(questionlist, many=True)

        return JsonResponse(serializer.data, safe=False)


def show_question(request):

    if request.method == 'GET':
        questions = Question.objects.order_by('question_number')
        serializer = QuestionSerializer(questions, many=True)

        return JsonResponse(serializer.data, safe=False)
