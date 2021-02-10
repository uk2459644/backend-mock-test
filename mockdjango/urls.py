"""mockdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mockapp.views import *
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = 'Mock-Test'
admin.site.site_title = 'Mock Test Admin'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_question),
     path('api-auth/', include('rest_framework.urls')),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # get language list
    path('lang/', get_language_list),

    # get categories list
    path('cat/', get_categories_list),
    path('preview/cat/', preview_get_categories_list),

    # get article info points and list
    path('article-info/', article_info_list),
    path('article-points-list/<int:cid>/', article_point_list),
    path('article-info/preview/', preview_article_info_list),

    # get job info and points list
    path('jobs-info/', job_info_list),
    path('jobs-points-list/<int:cid>/', job_point_list),
    path('jobs-info/preview/', preview_job_info_list),


    # privacy policy list , terms and faq
    path('privacy-policy/', privacy_policy_list),
    path('terms-list/', terms_list),
    path('faq/', faq_list),

    # list of test names by categories
    path('ssc-cgl-testlist/', ssc_cgl_testlist),
    path('ssc-chsl-testlist/', ssc_chsl_testlist),
    path('ssc-je-ee/', ssc_je_ee_testlist),
    path('ssc-je-ce/', ssc_je_ce_testlist),
    path('rrb-ntpc/', rrb_ntpc_testlist),
    path('rrb-group-d/', rrb_groupd_testlist),
    path('bihar-police/', bihar_police_testlist),

    # preview list of test names by categories
    path('ssc-cgl-testlist/preview/', preview_ssc_cgl_testlist),
    path('ssc-chsl-testlist/preview/', preview_ssc_chsl_testlist),
    path('ssc-je-ee/preview/', preview_ssc_je_ee_testlist),
    path('ssc-je-ce/preview/', preview_ssc_je_ee_testlist),
    path('rrb-ntpc/preview/', preview_rrb_ntpc_testlist),
    path('rrb-group-d/preview/', preview_rrb_groupd_testlist),
    path('bihar-police/preview/', preview_bihar_police_testlist),


    # list of previous year test names by categories
    path('previous-year-ssc-cgl-testlist/', ssc_cgl_testlist_previous_year),
    path('previous-year-ssc-chsl-testlist/', ssc_chsl_testlist_previous_year),
    path('previous-year-ssc-je-ee/', ssc_je_ee_testlist_previous_year),
    path('previous-year-ssc-je-ce/', ssc_je_ce_testlist_previous_year),
    path('previous-year-rrb-ntpc/', rrb_ntpc_testlist_previous_year),
    path('previous-year-rrb-group-d/', rrb_groupd_testlist_previous_year),

    # preview list of previous year test names by categories
    path('previous-year-ssc-cgl-testlist/preview/',
         preview_ssc_cgl_testlist_previous_year),
    path('previous-year-ssc-chsl-testlist/preview/',
         preview_ssc_chsl_testlist_previous_year),
    path('previous-year-ssc-je-ee/preview/',
         preview_ssc_je_ee_testlist_previous_year),
    path('previous-year-ssc-je-ce/preview/',
         preview_ssc_je_ce_testlist_previous_year),
    path('previous-year-rrb-ntpc/preview/',
         preview_rrb_ntpc_testlist_previous_year),
    path('previous-year-rrb-group-d/preview/',
         preview_rrb_ntpc_testlist_previous_year),

    # list of questions by test names
    path('rrb-ntpc/<int:cid>/', rrb_ntpc_questions_by_test_name),
    path('rrb-group-d/<int:cid>/', rrb_groupd_questions_by_test_name),
    path('ssc-je-ce/<int:cid>/', ssc_je_ce_questions_by_test_name),
    path('ssc-je-ee/<int:cid>/', ssc_je_ee_questions_by_test_name),
    path('ssc-chsl-testlist/<int:cid>/', ssc_chsl_questions_by_test_name),
    path('ssc-cgl-testlist/<int:cid>/', ssc_cgl_questions_by_test_name),
    path('bihar-police/<int:cid>/', bihar_police_questions_by_test_name),

    # previous year list of questions by test names
    path('previous-year-rrb-ntpc/<int:cid>/',
         previous_year_rrb_ntpc_questions_by_test_name),
    path('previous-year-rrb-group-d/<int:cid>/',
         previous_year_rrb_groupd_questions_by_test_name),
    path('previous-year-ssc-je-ce/<int:cid>/',
         previous_year_ssc_je_ce_questions_by_test_name),
    path('previous-year-ssc-je-ee/<int:cid>/',
         previous_year_ssc_je_ee_questions_by_test_name),
    path('previous-year-ssc-chsl-testlist/<int:cid>/',
         previous_year_ssc_chsl_questions_by_test_name),
    path('previous-year-ssc-cgl-testlist/<int:cid>/',
         previous_year_ssc_cgl_questions_by_test_name),

]
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
