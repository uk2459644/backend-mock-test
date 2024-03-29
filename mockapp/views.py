from django.shortcuts import render
from .models import *
from .serializers import *
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import render
from .forms import Question_Essential
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):

    if request.method == 'POST':
        form=Question_Essential(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            test_name=form.cleaned_data['test_name']
            month=form.cleaned_data['month']
            year=form.cleaned_data['year']
            category=form.cleaned_data['category']
            correct_mark=form.cleaned_data['correct_mark']
            negative_mark=form.cleaned_data['negative_mark']

            # q_model= QuestionBiharPolice(
            #     test_name= int(13),
            #     category= 7,
            #     subject= 1,
            #     month= 8,
            #     comprehension_show= False,
            #     comprehension_doc= False,
            #     question_doc= False,
            #     doc= False,
            #     comprehension= "s",
            #     year= 1,
            #     show= True,
            #     question= "s",
            #     a= "s",
            #     b= "s",
            #     c= "s",
            #     d= "s",
            #     correct_opt= "s",
            #     question_number= 14,
            #     correct_mark= 1.0,
            #     correct_text= "s",
            #     negative_mark= 0.0
            #        )
             
            print(request.POST)
          #  q_model.save()
        return HttpResponseRedirect('/')
            
    
    else:
        form=Question_Essential()
    
    return render(request,'index.html',{'form':form})


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

def previous__year_bihar_police_testlist(request):

    if request.method == 'GET':
        testlist = BiharPoliceTestName.objects.filter(
            is_previous_year_question=True,show_test=True).order_by('test_number')
        serializer = Bihar_Police_TestNameSerializer(testlist, many=True)
        return JsonResponse(serializer.data, safe=False)

def preview_bihar_police_testlist(request):

    if request.method == 'GET':
        testlist = BiharPoliceTestName.objects.filter(
            is_previous_year_question=False,show_test=False).order_by('test_number')
        serializer = Bihar_Police_TestNameSerializer(testlist, many=True)
        return JsonResponse(serializer.data, safe=False)

def preview_previous__year_bihar_police_testlist(request):

    if request.method == 'GET':
        testlist = BiharPoliceTestName.objects.filter(
            is_previous_year_question=True,show_test=False).order_by('test_number')
        serializer = Bihar_Police_TestNameSerializer(testlist, many=True)
        return JsonResponse(serializer.data, safe=False)
@csrf_exempt   
def bihar_police_questions_by_test_name(request, cid):
    if request.method == 'GET':
        questionlist = QuestionBiharPolice.objects.filter(
            test_name=cid).order_by('question_number')
        serializer = Bihar_Police_QuestionSerializer(questionlist, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        q_data=JSONParser().parse(request)
        q_serializer=Bihar_Police_QuestionSerializer(data=q_data)
        if q_serializer.is_valid():
            q_serializer.save()
            return JsonResponse(q_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(q_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'PUT':
        obj=QuestionBiharPolice.objects.get(pk=cid)
        q_data=JSONParser().parse(request)
        q_serializer=Bihar_Police_QuestionSerializer(obj,data=q_data,partial=True)
        if q_serializer.is_valid():
            q_serializer.save()
            return JsonResponse(q_serializer.data,status=status.HTTP_206_PARTIAL_CONTENT)
        return JsonResponse(q_serializer.errors,status.HTTP_400_BAD_REQUEST) 

# getting article info and points
def article_info_list(request):
    if request.method == 'GET':
        jobinfo_list=ArticleInfo.objects.filter(show=True).order_by('info_no')
        serializer=ArticleInfoSerializer(jobinfo_list,many=True)
        return JsonResponse(serializer.data,safe=False)

def preview_article_info_list(request):
    if request.method == 'GET':
        jobinfo_list=ArticleInfo.objects.filter(show=False).order_by('info_no')
        serializer=ArticleInfoSerializer(jobinfo_list,many=True)
        return JsonResponse(serializer.data,safe=False)

def article_point_list(request,cid):
    if request.method == 'GET':
        pointinfo_list=ArticleInfoPoints.objects.filter(job_info=cid).order_by('point_no')
        serializer=ArticleInfoPointSerializer(pointinfo_list,many=True)
        return JsonResponse(serializer.data,safe=False)

# getting job info and points

def job_info_list(request):
    if request.method == 'GET':
        jobinfo_list=JobInfo.objects.filter(show=True).order_by('info_no')
        serializer=JobInfoSerializer(jobinfo_list,many=True)
        return JsonResponse(serializer.data,safe=False)

def preview_job_info_list(request):
    if request.method == 'GET':
        jobinfo_list=JobInfo.objects.filter(show=False).order_by('info_no')
        serializer=JobInfoSerializer(jobinfo_list,many=True)
        return JsonResponse(serializer.data,safe=False)

def job_point_list(request,cid):
    if request.method == 'GET':
        pointinfo_list=JobInfoPoints.objects.filter(job_info=cid).order_by('point_no')
        serializer=JobInfoPointSerializer(pointinfo_list,many=True)
        return JsonResponse(serializer.data,safe=False)
#getting subject , test name by subject and questions related models here
def subject_list(request):
    if request.method == 'GET':
        jobinfo_list=Subject.objects.filter(show=True)
        serializer=SubjectSerializer(jobinfo_list,many=True)
        return JsonResponse(serializer.data,safe=False)

def test_list_by_subject(request,cid):
   if request.method == 'GET':
        jobinfo_list=SubjectByTestName.objects.filter(subject=cid)
        serializer=SubjectByTestNameSerializer(jobinfo_list,many=True)
        return JsonResponse(serializer.data,safe=False)
        
@csrf_exempt 
def questions_by_subject_test_name(request, cid):
    if request.method == 'GET':
        questionlist = QuestionBySubjectTestName.objects.filter(
            test_name=cid).order_by('question_number')
        serializer = QuestionBySubjectTestNameSerializer(questionlist, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        q_data=JSONParser().parse(request)
        q_serializer=QuestionBySubjectTestNameSerializer(data=q_data)
        if q_serializer.is_valid():
            q_serializer.save()
            return JsonResponse(q_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(q_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
       
    elif request.method == 'PUT':
        obj=QuestionBySubjectTestName.objects.get(pk=cid)
        q_data=JSONParser().parse(request)
        q_serializer=QuestionBySubjectTestNameSerializer(obj,data=q_data,partial=True)
        if q_serializer.is_valid():
            q_serializer.save()
            return JsonResponse(q_serializer.data,status=status.HTTP_206_PARTIAL_CONTENT)
        return JsonResponse(q_serializer.errors,status.HTTP_400_BAD_REQUEST)

# getting institute related models query response
def city_list(request):
   if request.method == 'GET':
        jobinfo_list=City.objects.filter(show=True)
        serializer=CitySerializer(jobinfo_list,many=True)
        return JsonResponse(serializer.data,safe=False)
        
def all_institute_list(request):
    if request.method == 'GET':
        jobinfo_list=Institute.objects.all()
        serializer=InstituteSerializer(jobinfo_list,many=True)
        return JsonResponse(serializer.data,safe=False)

def institute_list(request,cid):
    if request.method == 'GET':
        jobinfo_list=Institute.objects.filter(city=cid)
        serializer=InstituteSerializer(jobinfo_list,many=True)
        return JsonResponse(serializer.data,safe=False)

def test_list_by_institute(request,cid):
    if request.method == 'GET':
        jobinfo_list=InstituteTestName.objects.filter(institute=cid)
        serializer=InstituteTestNameSerializer(jobinfo_list,many=True)
        return JsonResponse(serializer.data,safe=False)


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

@csrf_exempt 
def ssc_cgl_questions_by_test_name(request, cid):
    if request.method == 'GET':
        questionlist = QuestionSSCCGL.objects.filter(
            test_name=cid).order_by('question_number')
        serializer = SSC_CGL_QuestionSerializer(questionlist, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        q_data=JSONParser().parse(request)
        q_serializer=SSC_CGL_QuestionSerializer(data=q_data)
        if q_serializer.is_valid():
            q_serializer.save()
            return JsonResponse(q_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(q_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
       
    elif request.method == 'PUT':
        obj=QuestionSSCCGL.objects.get(pk=cid)
        q_data=JSONParser().parse(request)
        q_serializer=SSC_CGL_QuestionSerializer(obj,data=q_data,partial=True)
        if q_serializer.is_valid():
            q_serializer.save()
            return JsonResponse(q_serializer.data,status=status.HTTP_206_PARTIAL_CONTENT)
        return JsonResponse(q_serializer.errors,status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
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

@csrf_exempt 
def ssc_chsl_questions_by_test_name(request, cid):
    if request.method == 'GET':
        questionlist = QuestionSSCCHSL.objects.filter(
            test_name=cid).order_by('question_number')
        serializer = SSC_CHSL_QuestionSerializer(questionlist, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        q_data=JSONParser().parse(request)
        q_serializer=SSC_CHSL_QuestionSerializer(data=q_data)
        if q_serializer.is_valid():
            q_serializer.save()
            return JsonResponse(q_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(q_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        obj=QuestionSSCCHSL.objects.get(pk=cid)
        q_data=JSONParser().parse(request)
        q_serializer=SSC_CHSL_QuestionSerializer(obj,data=q_data,partial=True)
        if q_serializer.is_valid():
            q_serializer.save()
            return JsonResponse(q_serializer.data,status=status.HTTP_206_PARTIAL_CONTENT)
        return JsonResponse(q_serializer.errors,status.HTTP_400_BAD_REQUEST)    
    

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

@csrf_exempt 
def ssc_je_ee_questions_by_test_name(request, cid):
    if request.method == 'GET':
        questionlist = QuestionSSCJEEE.objects.filter(
            test_name=cid).order_by('question_number')
        serializer = SSC_JE_EE_QuestionSerializer(questionlist, many=True)
        return JsonResponse(serializer.data, safe=False)
      
    elif request.method == 'PUT':
        obj=QuestionSSCJEEE.objects.get(pk=cid)
        q_data=JSONParser().parse(request)
        q_serializer=SSC_JE_EE_QuestionSerializer(obj,data=q_data,partial=True)
        if q_serializer.is_valid():
            q_serializer.save()
            return JsonResponse(q_serializer.data,status=status.HTTP_206_PARTIAL_CONTENT)
        return JsonResponse(q_serializer.errors,status.HTTP_400_BAD_REQUEST)

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

@csrf_exempt 
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

@csrf_exempt 
def rrb_ntpc_questions_by_test_name(request, cid):

    if request.method == 'GET':
        questionlist = QuestionRRBNtpc.objects.filter(
            test_name=cid).order_by('question_number')
        serializer = RRB_NTPC_QuestionSerializer(questionlist, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        q_data=JSONParser().parse(request)
        q_serializer=RRB_NTPC_QuestionSerializer(data=q_data)
        if q_serializer.is_valid():
            q_serializer.save()
            return JsonResponse(q_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(q_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      
    elif request.method == 'PUT':
        obj=QuestionRRBNtpc.objects.get(pk=cid)
        q_data=JSONParser().parse(request)
        q_serializer=RRB_NTPC_QuestionSerializer(obj,data=q_data,partial=True)
        if q_serializer.is_valid():
            q_serializer.save()
            return JsonResponse(q_serializer.data,status=status.HTTP_206_PARTIAL_CONTENT)
        return JsonResponse(q_serializer.errors,status.HTTP_400_BAD_REQUEST)

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

@csrf_exempt 
def rrb_groupd_questions_by_test_name(request, cid):
    if request.method == 'GET':
        questionlist = QuestionRRBGroupD.objects.filter(
            test_name=cid).order_by('question_number')
        serializer = RRB_GROUPD_QuestionSerializer(questionlist, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        q_data=JSONParser().parse(request)
        q_serializer=RRB_GROUPD_QuestionSerializer(data=q_data)
        if q_serializer.is_valid():
            q_serializer.save()
            return JsonResponse(q_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(q_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      
    elif request.method == 'PUT':
        obj=QuestionRRBGroupD.objects.get(pk=cid)
        q_data=JSONParser().parse(request)
        q_serializer=RRB_GROUPD_QuestionSerializer(obj,data=q_data,partial=True)
        if q_serializer.is_valid():
            q_serializer.save()
            return JsonResponse(q_serializer.data,status=status.HTTP_206_PARTIAL_CONTENT)
        return JsonResponse(q_serializer.errors,status.HTTP_400_BAD_REQUEST)

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
