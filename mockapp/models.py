from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# testlist by model


class FAQSSCChsl(models.Model):
    faq_no = models.IntegerField()
    faq_question = models.CharField(max_length=150, help_text='FAQ Question')
    faq_answer = models.TextField(help_text='Answer here .')
    show = models.BooleanField(default=False)
    

    class Meta:
        ordering = ['faq_no', 'faq_question', 'faq_answer', 'show']

    def __str__(self):
        return self.faq_question

# basic models here


class LanguageSelector(models.Model):
    lang_no = models.IntegerField(null=True, blank=True)
    lang_name = models.CharField(max_length=120, null=True, blank=True)
    show = models.BooleanField(default=True)

    class Meta:
        ordering = ['lang_name', 'lang_no', 'show']

    def __str__(self):
        return self.lang_name


class FAQ(models.Model):
    faq_no = models.IntegerField()
    faq_question = models.CharField(max_length=150, help_text='FAQ Question')
    faq_answer = models.TextField(help_text='Answer here .')
    show = models.BooleanField(default=False)

    class Meta:
        ordering = ['faq_no', 'faq_question', 'faq_answer', 'show']

    def __str__(self):
        return self.faq_question


class PrivacyPolicy(models.Model):
    policy_no = models.IntegerField()
    policy_title = models.CharField(max_length=150)
    policy_description = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=False)

    class Meta:
        ordering = ['policy_no', 'policy_title', 'policy_description', 'show']

    def __str__(self):
        return self.policy_title


class TermsCondition(models.Model):
    term_no = models.IntegerField()
    term_title = models.CharField(max_length=150)
    term_desc = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=False)

    class Meta:
        ordering = ['term_no', 'term_title', 'term_desc', 'show']

    def __str__(self):
        return self.term_title


class Year(models.Model):
    year = models.CharField(max_length=4)
    pub_date = models.DateField(auto_now=True)
    edit_date = models.DateField(auto_now=True)

    class Meta:
        ordering = ['year', 'pub_date', 'edit_date']

    def __str__(self):
        return self.year

# Previous year YEAR model


class PreviousYear(models.Model):
    year = models.CharField(max_length=4)
    pub_date = models.DateField(auto_now=True)
    edit_date = models.DateField(auto_now=True)

    class Meta:
        ordering = ['year', 'pub_date', 'edit_date']

    def __str__(self):
        return self.year


class Month(models.Model):
    month = models.CharField(max_length=20)
    pub_date = models.DateField(auto_now=True)
    edit_date = models.DateField(auto_now=True)

    class Meta:
        ordering = ['month', 'pub_date', 'edit_date']

    def __str__(self):
        return self.month

# storage info models here


class Information(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    info_no = models.IntegerField(null=True, blank=True)
    info_title = models.CharField(max_length=200)
    message = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['year', 'month', 'info_no', 'info_title', 'message']

    def __str__(self):
        return self.info_title


class TestCategory(models.Model):
    category = models.CharField(max_length=100)
    pub_date = models.DateField(auto_now=True)
    edit_date = models.DateField(auto_now=True)
    keyword = models.CharField(max_length=150, default='')
    previous_year_keyword = models.CharField(max_length=150, default='')
    preview_keyword = models.CharField(max_length=150, default='')
    preview_previous_year_keyword = models.CharField(
        max_length=150, default='')
    show = models.BooleanField(default=False)
    preview_show = models.BooleanField(default=False)

    class Meta:
        ordering = ['category', 'keyword', 'preview_keyword', 'pub_date', 'edit_date',
                    'previous_year_keyword', 'preview_previous_year_keyword', 'show',
                    'preview_show'
                    ]

    def __str__(self):
        return self.category


class Subject(models.Model):
    subject = models.CharField(max_length=150)
    pub_date = models.DateField(auto_now=True)
    edit_date = models.DateField(auto_now=True)

    class Meta:
        ordering = ['subject', 'pub_date', 'edit_date']

    def __str__(self):
        return self.subject


class TestName(models.Model):
    lang = models.ForeignKey(
        LanguageSelector, on_delete=models.CASCADE, null=True, blank=True)
    test_number = models.IntegerField(null=True, blank=True)
    test_name = models.CharField(max_length=120)
    keyword = models.CharField(max_length=120, null=True, blank=True)
    is_previous_year_question = models.BooleanField(default=False)
    total_no_of_question = models.IntegerField(null=True, blank=True)
    month = models.ForeignKey(
        Month, on_delete=models.CASCADE, null=True, blank=True)
    year = models.ForeignKey(
        Year, on_delete=models.CASCADE, null=True, blank=True)
    pub_date = models.DateField()
    edit_date = models.DateField()
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)

    class Meta:
        ordering = ['test_number', 'year', 'month',
                    'is_previous_year_question',
                    'total_no_of_question',
                    'test_name', 'pub_date', 'edit_date', 'category']

    def __str__(self):
        return self.test_name

# Article and points models are here


class ArticleInfo(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    month = models.ForeignKey(
        Month, on_delete=models.SET_NULL, null=True, blank=True)
    year = models.ForeignKey(
        Year, on_delete=models.SET_NULL, null=True, blank=True)
    info_no = models.IntegerField(null=True, blank=True)
    keyword = models.CharField(max_length=120, null=True, blank=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        TestCategory, on_delete=models.SET_NULL, null=True, blank=True)
    cat_text = models.CharField(
        max_length=150, help_text='Write category in text, which is choosen above.')
    image = models.TextField(null=True, blank=True)
    show = models.BooleanField(default=True)

    class Meta:
        ordering = ['pub_date', 'title', 'short_description', 'category',
                    'cat_text', 'month', 'year', 'image', 'info_no', 'keyword', 'show'
                    ]

    def __str__(self):
        return self.title


class ArticleInfoPoints(models.Model):
    point_no = models.IntegerField(null=True, blank=True)
    job_info = models.ForeignKey(ArticleInfo, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    show = models.BooleanField(default=True)
    image_show = models.BooleanField(default=False)
    image_url = models.TextField(
        null=True, blank=True, help_text='Paste image url here.')

    class Meta:
        ordering = ['point_no', 'job_info', 'title',
                    'description', 'show', 'image_show', 'image_url']

    def __str__(self):
        return self.title

# Job Info models are here

class JobCategory(models.Model):
    category = models.CharField(max_length=100)
    pub_date = models.DateField(auto_now=True)
    edit_date = models.DateField(auto_now=True)
    keyword = models.CharField(max_length=150, default='')
    previous_year_keyword = models.CharField(max_length=150, default='')
    preview_keyword = models.CharField(max_length=150, default='')
    preview_previous_year_keyword = models.CharField(
        max_length=150, default='')
    show = models.BooleanField(default=False)
    preview_show = models.BooleanField(default=False)

    class Meta:
        ordering = ['category', 'keyword', 'preview_keyword', 'pub_date', 'edit_date',
                    'previous_year_keyword', 'preview_previous_year_keyword', 'show',
                    'preview_show'
                    ]

    def __str__(self):
        return self.category



class JobInfo(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    month = models.ForeignKey(
        Month, on_delete=models.SET_NULL, null=True, blank=True)
    year = models.ForeignKey(
        Year, on_delete=models.SET_NULL, null=True, blank=True)
    info_no = models.IntegerField(null=True, blank=True)
    keyword = models.CharField(max_length=120, null=True, blank=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        TestCategory, on_delete=models.SET_NULL, null=True, blank=True,default=1)
    category_job = models.ForeignKey(
        JobCategory, on_delete=models.SET_NULL, null=True, blank=True,default="")
    cat_text = models.CharField(
        max_length=150, help_text='Write category in text, which is choosen above.')
    image = models.TextField(null=True, blank=True)
    show = models.BooleanField(default=True)

    class Meta:
        ordering = ['pub_date', 'title', 'short_description', 'category','category_job',
                    'cat_text', 'month', 'year', 'image', 'info_no', 'keyword', 'show'
                    ,'user']

    def __str__(self):
        return self.title


class JobInfoPoints(models.Model):
    point_no = models.IntegerField(null=True, blank=True)
    job_info = models.ForeignKey(JobInfo, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    show = models.BooleanField(default=True)
    image_show = models.BooleanField(default=False)
    image_url = models.TextField(
        null=True, blank=True, help_text='Paste image url here.')

    class Meta:
        ordering = ['point_no', 'job_info', 'title',
                    'description', 'show', 'image_show', 'image_url']

    def __str__(self):
        return self.title

# BIHAR POLICE Test name models here


class BiharPoliceTestName(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    language = models.ForeignKey(
        LanguageSelector, on_delete=models.CASCADE, null=True, blank=True, default='')
    test_number = models.IntegerField(null=True, blank=True)
    test_name = models.CharField(max_length=120)
    keyword = models.CharField(max_length=120, null=True, blank=True)
    is_previous_year_question = models.BooleanField(default=False)
    total_no_of_question = models.IntegerField(null=True, blank=True)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    pub_date = models.DateField()
    edit_date = models.DateField()
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    show_test = models.BooleanField(default=True)
    test_time = models.IntegerField(
        default=60, help_text='test time in minutes')

    class Meta:
        ordering = ['test_number', 'year', 'month', 'show_test','user',
                    'is_previous_year_question',
                    'total_no_of_question',
                    'language',
                    'test_name', 'test_time',
                    'pub_date', 'edit_date', 'category']

    def __str__(self):
        return self.test_name


# RRB Test name models here


class RRBGroupDTestName(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    language = models.ForeignKey(
        LanguageSelector, on_delete=models.CASCADE, null=True, blank=True, default='')
    test_number = models.IntegerField(null=True, blank=True)
    test_name = models.CharField(max_length=120)
    keyword = models.CharField(max_length=120, null=True, blank=True)
    is_previous_year_question = models.BooleanField(default=False)
    total_no_of_question = models.IntegerField(null=True, blank=True)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    pub_date = models.DateField()
    edit_date = models.DateField()
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    show_test = models.BooleanField(default=True)
    test_time = models.IntegerField(
        default=60, help_text='test time in minutes')

    class Meta:
        ordering = ['test_number', 'year', 'month', 'show_test','user',
                    'is_previous_year_question',
                    'total_no_of_question',
                    'language',
                    'test_name', 'test_time', 'pub_date', 'edit_date', 'category']

    def __str__(self):
        return self.test_name


class RRBNtpcTestName(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    language = models.ForeignKey(
        LanguageSelector, on_delete=models.CASCADE, null=True, blank=True, default='')
    test_number = models.IntegerField(null=True, blank=True)
    test_name = models.CharField(max_length=120)
    keyword = models.CharField(max_length=120, null=True, blank=True)
    is_previous_year_question = models.BooleanField(default=False)
    total_no_of_question = models.IntegerField(null=True, blank=True)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    pub_date = models.DateField()
    edit_date = models.DateField()
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    show_test = models.BooleanField(default=True)
    test_time = models.IntegerField(
        default=60, help_text='test time in minutes')

    class Meta:
        ordering = ['test_number', 'year', 'month', 'show_test','user',
                    'is_previous_year_question',
                    'total_no_of_question',
                    'language',
                    'test_name', 'test_time', 'pub_date', 'edit_date', 'category']

    def __str__(self):
        return self.test_name

# Previous year RRB TEST names here


class PreviousYearRRBGroupDTestName(models.Model):
    language = models.ForeignKey(
        LanguageSelector, on_delete=models.CASCADE, null=True, blank=True, default='')
    test_number = models.IntegerField(null=True, blank=True)
    test_name = models.CharField(max_length=120)
    keyword = models.CharField(max_length=120, null=True, blank=True)
    is_previous_year_question = models.BooleanField(default=False)
    total_no_of_question = models.IntegerField(null=True, blank=True)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(PreviousYear, on_delete=models.CASCADE)
    pub_date = models.DateField()
    edit_date = models.DateField()
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    show_test = models.BooleanField(default=True)
    test_time = models.IntegerField(
        default=60, help_text='test time in minutes')

    class Meta:
        ordering = ['test_number', 'year', 'month', 'show_test',
                    'is_previous_year_question',
                    'total_no_of_question',
                    'language',
                    'test_name', 'test_time', 'pub_date', 'edit_date', 'category']

    def __str__(self):
        return self.test_name


class PreviousYearRRBNtpcTestName(models.Model):
    language = models.ForeignKey(
        LanguageSelector, on_delete=models.CASCADE, null=True, blank=True, default='')
    test_number = models.IntegerField(null=True, blank=True)
    test_name = models.CharField(max_length=120)
    keyword = models.CharField(max_length=120, null=True, blank=True)
    is_previous_year_question = models.BooleanField(default=False)
    total_no_of_question = models.IntegerField(null=True, blank=True)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(PreviousYear, on_delete=models.CASCADE)
    pub_date = models.DateField()
    edit_date = models.DateField()
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    show_test = models.BooleanField(default=True)
    test_time = models.IntegerField(
        default=60, help_text='test time in minutes')

    class Meta:
        ordering = ['test_number', 'year', 'month', 'show_test',
                    'is_previous_year_question',
                    'total_no_of_question',
                    'language',
                    'test_name', 'test_time', 'pub_date', 'edit_date', 'category']

    def __str__(self):
        return self.test_name


# SSC Test name models here


class SscJeCeTestName(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    language = models.ForeignKey(
        LanguageSelector, on_delete=models.CASCADE, null=True, blank=True, default='')
    test_number = models.IntegerField(null=True, blank=True)
    test_name = models.CharField(max_length=120)
    keyword = models.CharField(max_length=120, null=True, blank=True)
    is_previous_year_question = models.BooleanField(default=False)
    total_no_of_question = models.IntegerField(null=True, blank=True)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    pub_date = models.DateField()
    edit_date = models.DateField()
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    show_test = models.BooleanField(default=True)
    test_time = models.IntegerField(
        default=60, help_text='test time in minutes')

    class Meta:
        ordering = ['test_number', 'year', 'month', 'show_test','user',
                    'is_previous_year_question',
                    'total_no_of_question',
                    'language',
                    'test_name', 'test_time', 'pub_date', 'edit_date', 'category']

    def __str__(self):
        return self.test_name


class SSCJEEETestName(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    language = models.ForeignKey(
        LanguageSelector, on_delete=models.CASCADE, null=True, blank=True, default='')
    test_number = models.IntegerField(null=True, blank=True)
    test_name = models.CharField(max_length=120)
    keyword = models.CharField(max_length=120, null=True, blank=True)
    is_previous_year_question = models.BooleanField(default=False)
    total_no_of_question = models.IntegerField(null=True, blank=True)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    pub_date = models.DateField()
    edit_date = models.DateField()
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    show_test = models.BooleanField(default=True)
    test_time = models.IntegerField(
        default=60, help_text='test time in minutes')

    class Meta:
        ordering = ['test_number', 'year', 'month', 'show_test','user',
                    'is_previous_year_question',
                    'total_no_of_question',
                    'language',
                    'test_name', 'test_time', 'pub_date', 'edit_date', 'category']

    def __str__(self):
        return self.test_name


class SSCCHSLTestName(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    language = models.ForeignKey(
        LanguageSelector, on_delete=models.CASCADE, null=True, blank=True, default='')
    test_number = models.IntegerField(null=True, blank=True)
    test_name = models.CharField(max_length=120)
    keyword = models.CharField(max_length=120, null=True, blank=True)
    is_previous_year_question = models.BooleanField(default=False)
    total_no_of_question = models.IntegerField(null=True, blank=True)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    pub_date = models.DateField()
    edit_date = models.DateField()
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    show_test = models.BooleanField(default=True)
    test_time = models.IntegerField(
        default=60, help_text='test time in minutes')

    class Meta:
        ordering = ['test_number', 'year', 'month', 'show_test','user',
                    'is_previous_year_question',
                    'total_no_of_question',
                    'language',
                    'test_name', 'test_time', 'pub_date', 'edit_date', 'category']

    def __str__(self):
        return self.test_name


class SSCCGLTestName(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    language = models.ForeignKey(
        LanguageSelector, on_delete=models.CASCADE, null=True, blank=True, default='')
    test_number = models.IntegerField(null=True, blank=True)
    test_name = models.CharField(max_length=120)
    keyword = models.CharField(max_length=120, null=True, blank=True)
    is_previous_year_question = models.BooleanField(default=False)
    total_no_of_question = models.IntegerField(null=True, blank=True)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    pub_date = models.DateField()
    edit_date = models.DateField()
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    show_test = models.BooleanField(default=True)
    test_time = models.IntegerField(
        default=60, help_text='test time in minutes')

    class Meta:
        ordering = ['test_number', 'year', 'month', 'show_test','user',
                    'is_previous_year_question',
                    'total_no_of_question',
                    'language',
                    'test_name', 'test_time', 'pub_date', 'edit_date', 'category']

    def __str__(self):
        return self.test_name

# Previous Year SSC TEST name models here


class PreviousYearSscJeCeTestName(models.Model):
    language = models.ForeignKey(
        LanguageSelector, on_delete=models.CASCADE, null=True, blank=True, default='')
    test_number = models.IntegerField(null=True, blank=True)
    test_name = models.CharField(max_length=120)
    keyword = models.CharField(max_length=120, null=True, blank=True)
    is_previous_year_question = models.BooleanField(default=False)
    total_no_of_question = models.IntegerField(null=True, blank=True)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(PreviousYear, on_delete=models.CASCADE)
    pub_date = models.DateField()
    edit_date = models.DateField()
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    show_test = models.BooleanField(default=True)
    test_time = models.IntegerField(
        default=60, help_text='test time in minutes')

    class Meta:
        ordering = ['test_number', 'year', 'month', 'show_test',
                    'is_previous_year_question',
                    'total_no_of_question',
                    'language',
                    'test_name', 'test_time', 'pub_date', 'edit_date', 'category']

    def __str__(self):
        return self.test_name


class PreviousYearSSCJEEETestName(models.Model):
    language = models.ForeignKey(
        LanguageSelector, on_delete=models.CASCADE, null=True, blank=True, default='')
    test_number = models.IntegerField(null=True, blank=True)
    test_name = models.CharField(max_length=120)
    keyword = models.CharField(max_length=120, null=True, blank=True)
    is_previous_year_question = models.BooleanField(default=False)
    total_no_of_question = models.IntegerField(null=True, blank=True)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(PreviousYear, on_delete=models.CASCADE)
    pub_date = models.DateField()
    edit_date = models.DateField()
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    show_test = models.BooleanField(default=True)
    test_time = models.IntegerField(
        default=60, help_text='test time in minutes')

    class Meta:
        ordering = ['test_number', 'year', 'month', 'show_test',
                    'is_previous_year_question',
                    'total_no_of_question',
                    'language',
                    'test_name', 'test_time', 'pub_date', 'edit_date', 'category']

    def __str__(self):
        return self.test_name


class PreviousYearSSCCHSLTestName(models.Model):
    language = models.ForeignKey(
        LanguageSelector, on_delete=models.CASCADE, null=True, blank=True, default='')
    test_number = models.IntegerField(null=True, blank=True)
    test_name = models.CharField(max_length=120)
    keyword = models.CharField(max_length=120, null=True, blank=True)
    is_previous_year_question = models.BooleanField(default=False)
    total_no_of_question = models.IntegerField(null=True, blank=True)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(PreviousYear, on_delete=models.CASCADE)
    pub_date = models.DateField()
    edit_date = models.DateField()
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    show_test = models.BooleanField(default=True)
    test_time = models.IntegerField(
        default=60, help_text='test time in minutes')

    class Meta:
        ordering = ['test_number', 'year', 'month', 'show_test',
                    'is_previous_year_question',
                    'total_no_of_question',
                    'language',
                    'test_name', 'test_time', 'pub_date', 'edit_date', 'category']

    def __str__(self):
        return self.test_name


class PreviousYearSSCCGLTestName(models.Model):
    language = models.ForeignKey(
        LanguageSelector, on_delete=models.CASCADE, null=True, blank=True, default='')
    test_number = models.IntegerField(null=True, blank=True)
    test_name = models.CharField(max_length=120)
    keyword = models.CharField(max_length=120, null=True, blank=True)
    is_previous_year_question = models.BooleanField(default=False)
    total_no_of_question = models.IntegerField(null=True, blank=True)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(PreviousYear, on_delete=models.CASCADE)
    pub_date = models.DateField()
    edit_date = models.DateField()
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    show_test = models.BooleanField(default=True)
    test_time = models.IntegerField(
        default=60, help_text='test time in minutes')

    class Meta:
        ordering = ['test_number', 'year', 'month', 'show_test',
                    'is_previous_year_question',
                    'total_no_of_question',
                    'language',
                    'test_name', 'test_time', 'pub_date', 'edit_date', 'category']

    def __str__(self):
        return self.test_name


class Question(models.Model):
    # pub_date = models.DateField()
    # edit_date = models.DateField()
    test_name = models.ForeignKey(TestName, on_delete=models.CASCADE)
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    comprehension_show = models.BooleanField(default=False)
    comprehension_doc = models.BooleanField(default=False)
    comprehension = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=True)
    question_doc = models.BooleanField(default=False)
    question_number = models.IntegerField(null=True, blank=True)
    question = models.TextField(help_text='Write question')
    doc = models.BooleanField(default=False)
    a = models.TextField(help_text='Option a')
    b = models.TextField(help_text='Option b')
    c = models.TextField(help_text='Option c')
    d = models.TextField(help_text='Option d')
    correct_opt = models.CharField(max_length=1)

    class Meta:
        ordering = ['test_name', 'category',
                    'subject', 'month', 'year', 'show', 'question', 'a', 'b',
                    'c', 'd', 'correct_opt', 'question_number']

    def __str__(self):
        return self.question

# Bihar Police Questioin model here


class QuestionBiharPolice(models.Model):
    # pub_date = models.DateField()
    # edit_date = models.DateField()
    test_name = models.ForeignKey(
        BiharPoliceTestName, on_delete=models.CASCADE, related_name='questionbiharpolice')
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    comprehension_show = models.BooleanField(default=False)
    comprehension_doc = models.BooleanField(default=False)
    comprehension = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=True)
    question_doc = models.BooleanField(default=False)
    question_number = models.IntegerField(null=True, blank=True)
    question = models.TextField(help_text='Write question')
    doc = models.BooleanField(default=False)
    a = models.TextField(help_text='Option a')
    b = models.TextField(help_text='Option b')
    c = models.TextField(help_text='Option c')
    d = models.TextField(help_text='Option d')
    correct_opt = models.CharField(max_length=1)
    correct_text = models.TextField(
        default='', help_text='Correct option value')
    correct_mark = models.FloatField(default=1)
    negative_mark = models.FloatField(default=0)

    class Meta:
        ordering = ['test_name', 'category',
                    'subject', 'month', 'year', 'show', 'question', 'a', 'b',
                    'c', 'd', 'correct_opt', 'question_number',
                    'correct_mark', 'correct_text', 'correct_text',
                    'negative_mark']

    def __str__(self):
        return self.question


# SSC Question models here


class QuestionSSCCGL(models.Model):
    # pub_date = models.DateField()
    # edit_date = models.DateField()
    test_name = models.ForeignKey(SSCCGLTestName, on_delete=models.CASCADE)
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    comprehension_show = models.BooleanField(default=False)
    comprehension_doc = models.BooleanField(default=False)
    comprehension = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=True)
    question_doc = models.BooleanField(default=False)
    question_number = models.IntegerField(null=True, blank=True)
    question = models.TextField(help_text='Write question')
    doc = models.BooleanField(default=False)
    a = models.TextField(help_text='Option a')
    b = models.TextField(help_text='Option b')
    c = models.TextField(help_text='Option c')
    d = models.TextField(help_text='Option d')
    correct_opt = models.CharField(max_length=1)
    correct_text = models.TextField(
        default='', help_text='Correct option value')
    correct_mark = models.FloatField(default=1)
    negative_mark = models.FloatField(default=0.5)

    class Meta:
        ordering = ['test_name', 'category',
                    'subject', 'month', 'year', 'show', 'question', 'a', 'b',
                    'c', 'd', 'correct_opt', 'question_number',
                    'correct_mark', 'correct_text', 'negative_mark']

    def __str__(self):
        return self.question


class QuestionSSCJECE(models.Model):
    # pub_date = models.DateField()
    # edit_date = models.DateField()
    test_name = models.ForeignKey(SscJeCeTestName, on_delete=models.CASCADE)
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    comprehension_show = models.BooleanField(default=False)
    comprehension_doc = models.BooleanField(default=False)
    comprehension = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=True)
    question_doc = models.BooleanField(default=False)
    question_number = models.IntegerField(null=True, blank=True)
    question = models.TextField(help_text='Write question')
    doc = models.BooleanField(default=False)
    a = models.TextField(help_text='Option a')
    b = models.TextField(help_text='Option b')
    c = models.TextField(help_text='Option c')
    d = models.TextField(help_text='Option d')
    correct_opt = models.CharField(max_length=1)
    correct_text = models.TextField(
        default='', help_text='Correct option value')
    correct_mark = models.FloatField(default=1)
    negative_mark = models.FloatField(default=0)

    class Meta:
        ordering = ['test_name', 'category',
                    'subject', 'month', 'year', 'show', 'question', 'a', 'b',
                    'c', 'd', 'correct_opt', 'question_number',
                    'correct_mark', 'correct_text', 'negative_mark']

    def __str__(self):
        return self.question


class QuestionSSCJEEE(models.Model):
    # pub_date = models.DateField()
    # edit_date = models.DateField()
    test_name = models.ForeignKey(SSCJEEETestName, on_delete=models.CASCADE)
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    comprehension_show = models.BooleanField(default=False)
    comprehension_doc = models.BooleanField(default=False)
    comprehension = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=True)
    question_doc = models.BooleanField(default=False)
    question_number = models.IntegerField(null=True, blank=True)
    question = models.TextField(help_text='Write question')
    doc = models.BooleanField(default=False)
    a = models.TextField(help_text='Option a')
    b = models.TextField(help_text='Option b')
    c = models.TextField(help_text='Option c')
    d = models.TextField(help_text='Option d')
    correct_opt = models.CharField(max_length=1)
    correct_text = models.TextField(
        default='', help_text='Correct option value')
    correct_mark = models.FloatField(default=1)
    negative_mark = models.FloatField(default=0)

    class Meta:
        ordering = ['test_name', 'category',
                    'subject', 'month', 'year', 'show', 'question', 'a', 'b',
                    'c', 'd', 'correct_opt', 'question_number',
                    'correct_mark', 'correct_text', 'negative_mark']

    def __str__(self):
        return self.question


class QuestionSSCCHSL(models.Model):
    # pub_date = models.DateField()
    # edit_date = models.DateField()
    test_name = models.ForeignKey(SSCCHSLTestName, on_delete=models.CASCADE)
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    comprehension_show = models.BooleanField(default=False)
    comprehension_doc = models.BooleanField(default=False)
    comprehension = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=True)
    question_doc = models.BooleanField(default=False)
    question_number = models.IntegerField(null=True, blank=True)
    question = models.TextField(help_text='Write question')
    doc = models.BooleanField(default=False)
    a = models.TextField(help_text='Option a')
    b = models.TextField(help_text='Option b')
    c = models.TextField(help_text='Option c')
    d = models.TextField(help_text='Option d')
    correct_opt = models.CharField(max_length=1)
    correct_text = models.TextField(
        default='', help_text='Correct option value')
    correct_mark = models.FloatField(default=1)
    negative_mark = models.FloatField(default=0.25)

    class Meta:
        ordering = ['test_name', 'category',
                    'subject', 'month', 'year', 'show', 'question', 'a', 'b',
                    'c', 'd', 'correct_opt', 'question_number',
                    'correct_mark', 'correct_text', 'negative_mark']

    def __str__(self):
        return self.question

# Previous year SSC questions models here


class PreviousYearQuestionSSCCGL(models.Model):
    # pub_date = models.DateField()
    # edit_date = models.DateField()
    test_name = models.ForeignKey(
        PreviousYearSSCCGLTestName, on_delete=models.CASCADE)
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(PreviousYear, on_delete=models.CASCADE)
    comprehension_show = models.BooleanField(default=False)
    comprehension_doc = models.BooleanField(default=False)
    comprehension = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=True)
    question_doc = models.BooleanField(default=False)
    question_number = models.IntegerField(null=True, blank=True)
    question = models.TextField(help_text='Write question')
    doc = models.BooleanField(default=False)
    a = models.TextField(help_text='Option a')
    b = models.TextField(help_text='Option b')
    c = models.TextField(help_text='Option c')
    d = models.TextField(help_text='Option d')
    correct_opt = models.CharField(max_length=1)
    correct_text = models.TextField(
        default='', help_text='Correct option value')
    correct_mark = models.FloatField(default=1)
    negative_mark = models.FloatField(default=0)

    class Meta:
        ordering = ['test_name', 'category',
                    'subject', 'month', 'year', 'show', 'question', 'a', 'b',
                    'c', 'd', 'correct_opt', 'question_number',
                    'correct_mark', 'correct_text', 'negative_mark']

    def __str__(self):
        return self.question


class PreviousYearQuestionSSCJECE(models.Model):
    # pub_date = models.DateField()
    # edit_date = models.DateField()
    test_name = models.ForeignKey(
        PreviousYearSscJeCeTestName, on_delete=models.CASCADE)
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(PreviousYear, on_delete=models.CASCADE)
    comprehension_show = models.BooleanField(default=False)
    comprehension_doc = models.BooleanField(default=False)
    comprehension = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=True)
    question_doc = models.BooleanField(default=False)
    question_number = models.IntegerField(null=True, blank=True)
    question = models.TextField(help_text='Write question')
    doc = models.BooleanField(default=False)
    a = models.TextField(help_text='Option a')
    b = models.TextField(help_text='Option b')
    c = models.TextField(help_text='Option c')
    d = models.TextField(help_text='Option d')
    correct_opt = models.CharField(max_length=1)
    correct_text = models.TextField(
        default='', help_text='Correct option value')
    correct_mark = models.FloatField(default=1)
    negative_mark = models.FloatField(default=0)

    class Meta:
        ordering = ['test_name', 'category',
                    'subject', 'month', 'year', 'show', 'question', 'a', 'b',
                    'c', 'd', 'correct_opt', 'question_number',
                    'correct_mark', 'correct_text', 'negative_mark']

    def __str__(self):
        return self.question


class PreviousYearQuestionSSCJEEE(models.Model):
    # pub_date = models.DateField()
    # edit_date = models.DateField()
    test_name = models.ForeignKey(
        PreviousYearSSCJEEETestName, on_delete=models.CASCADE)
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(PreviousYear, on_delete=models.CASCADE)
    comprehension_show = models.BooleanField(default=False)
    comprehension_doc = models.BooleanField(default=False)
    comprehension = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=True)
    question_doc = models.BooleanField(default=False)
    question_number = models.IntegerField(null=True, blank=True)
    question = models.TextField(help_text='Write question')
    doc = models.BooleanField(default=False)
    a = models.TextField(help_text='Option a')
    b = models.TextField(help_text='Option b')
    c = models.TextField(help_text='Option c')
    d = models.TextField(help_text='Option d')
    correct_opt = models.CharField(max_length=1)
    correct_text = models.TextField(
        default='', help_text='Correct option value')
    correct_mark = models.FloatField(default=1)
    negative_mark = models.FloatField(default=0)

    class Meta:
        ordering = ['test_name', 'category',
                    'subject', 'month', 'year', 'show', 'question', 'a', 'b',
                    'c', 'd', 'correct_opt', 'question_number',
                    'correct_mark', 'correct_text', 'negative_mark']

    def __str__(self):
        return self.question


class PreviousYearQuestionSSCCHSL(models.Model):
    # pub_date = models.DateField()
    # edit_date = models.DateField()
    test_name = models.ForeignKey(
        PreviousYearSSCCHSLTestName, on_delete=models.CASCADE)
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(PreviousYear, on_delete=models.CASCADE)
    comprehension_show = models.BooleanField(default=False)
    comprehension_doc = models.BooleanField(default=False)
    comprehension = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=True)
    question_doc = models.BooleanField(default=False)
    question_number = models.IntegerField(null=True, blank=True)
    question = models.TextField(help_text='Write question')
    doc = models.BooleanField(default=False)
    a = models.TextField(help_text='Option a')
    b = models.TextField(help_text='Option b')
    c = models.TextField(help_text='Option c')
    d = models.TextField(help_text='Option d')
    correct_opt = models.CharField(max_length=1)
    correct_text = models.TextField(
        default='', help_text='Correct option value')
    correct_mark = models.FloatField(default=1)
    negative_mark = models.FloatField(default=0)

    class Meta:
        ordering = ['test_name', 'category',
                    'subject', 'month', 'year', 'show', 'question', 'a', 'b',
                    'c', 'd', 'correct_opt', 'question_number',
                    'correct_mark', 'correct_text', 'negative_mark']

    def __str__(self):
        return self.question


# RRB Question models here


class QuestionRRBGroupD(models.Model):

    test_name = models.ForeignKey(RRBGroupDTestName, on_delete=models.CASCADE)
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    comprehension_show = models.BooleanField(default=False)
    comprehension_doc = models.BooleanField(default=False)
    comprehension = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=True)
    question_doc = models.BooleanField(default=False)
    question_number = models.IntegerField(null=True, blank=True)
    question = models.TextField(help_text='Write question')
    doc = models.BooleanField(default=False)
    a = models.TextField(help_text='Option a')
    b = models.TextField(help_text='Option b')
    c = models.TextField(help_text='Option c')
    d = models.TextField(help_text='Option d')
    correct_opt = models.CharField(max_length=1)
    correct_text = models.TextField(
        default='', help_text='Correct option value')
    correct_mark = models.FloatField(default=1)
    negative_mark = models.FloatField(default=0.33)

    class Meta:
        ordering = ['test_name', 'category',
                    'subject', 'month', 'year', 'show', 'question', 'a', 'b',
                    'c', 'd', 'correct_opt', 'question_number',
                    'correct_mark', 'correct_text', 'negative_mark']

    def __str__(self):
        return self.question


class QuestionRRBNtpc(models.Model):
    # pub_date = models.DateField()
    # edit_date = models.DateField()
    test_name = models.ForeignKey(RRBNtpcTestName, on_delete=models.CASCADE)
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    comprehension_show = models.BooleanField(default=False)
    comprehension_doc = models.BooleanField(default=False)
    comprehension = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=True)
    question_doc = models.BooleanField(default=False)
    question_number = models.IntegerField(null=True, blank=True)
    question = models.TextField(help_text='Write question')
    doc = models.BooleanField(default=False)
    a = models.TextField(help_text='Option a')
    b = models.TextField(help_text='Option b')
    c = models.TextField(help_text='Option c')
    d = models.TextField(help_text='Option d')
    correct_opt = models.CharField(max_length=1)
    correct_text = models.TextField(
        default='', help_text='Correct option value')
    correct_mark = models.FloatField(default=1)
    negative_mark = models.FloatField(default=0.33)

    class Meta:
        ordering = ['test_name', 'category',
                    'subject', 'month', 'year', 'show', 'question', 'a', 'b',
                    'c', 'd', 'correct_opt', 'question_number',
                    'correct_mark', 'correct_text', 'negative_mark']

    def __str__(self):
        return self.question

# Previous year RRB  question models here


class PreviousYearQuestionRRBGroupD(models.Model):
    # pub_date = models.DateField()
    # edit_date = models.DateField()
    test_name = models.ForeignKey(
        PreviousYearRRBGroupDTestName, on_delete=models.CASCADE)
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(PreviousYear, on_delete=models.CASCADE)
    comprehension_show = models.BooleanField(default=False)
    comprehension_doc = models.BooleanField(default=False)
    comprehension = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=True)
    question_doc = models.BooleanField(default=False)
    question_number = models.IntegerField(null=True, blank=True)
    question = models.TextField(help_text='Write question')
    doc = models.BooleanField(default=False)
    a = models.TextField(help_text='Option a')
    b = models.TextField(help_text='Option b')
    c = models.TextField(help_text='Option c')
    d = models.TextField(help_text='Option d')
    correct_opt = models.CharField(max_length=1)
    correct_text = models.TextField(
        default='', help_text='Correct option value')
    correct_mark = models.FloatField(default=1)
    negative_mark = models.FloatField(default=0.33)

    class Meta:
        ordering = ['test_name', 'category',
                    'subject', 'month', 'year', 'show', 'question', 'a', 'b',
                    'c', 'd', 'correct_opt', 'question_number',
                    'correct_mark', 'correct_text', 'negative_mark']

    def __str__(self):
        return self.question


class PreviousYearQuestionRRBNtpc(models.Model):
    # pub_date = models.DateField()
    # edit_date = models.DateField()
    test_name = models.ForeignKey(
        PreviousYearRRBNtpcTestName, on_delete=models.CASCADE)
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(PreviousYear, on_delete=models.CASCADE)
    comprehension_show = models.BooleanField(default=False)
    comprehension_doc = models.BooleanField(default=False)
    comprehension = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=True)
    question_doc = models.BooleanField(default=False)
    question_number = models.IntegerField(null=True, blank=True)
    question = models.TextField(help_text='Write question')
    doc = models.BooleanField(default=False)
    a = models.TextField(help_text='Option a')
    b = models.TextField(help_text='Option b')
    c = models.TextField(help_text='Option c')
    d = models.TextField(help_text='Option d')
    correct_opt = models.CharField(max_length=1)
    correct_text = models.TextField(
        default='', help_text='Correct option value')
    correct_mark = models.FloatField(default=1)
    negative_mark = models.FloatField(default=0.33)

    class Meta:
        ordering = ['test_name', 'category',
                    'subject', 'month', 'year', 'show', 'question', 'a', 'b',
                    'c', 'd', 'correct_opt', 'question_number',
                    'correct_mark', 'correct_text', 'negative_mark']

    def __str__(self):
        return self.question
