from django import forms

class Question_Essential(forms.Form):
    url=forms.URLField(label='test url', required=True)
    q_from=forms.IntegerField(label='q from', required=True)
    q_to=forms.IntegerField(label='q to', required=True)
    test_name=forms.IntegerField(label='test id',  required=True)
    category=forms.IntegerField(label='category id', required=True)
    subject=forms.IntegerField(label='subject id', required=True)
    month=forms.IntegerField(label='month id', required=True)
    year=forms.IntegerField(label='year id', required=True)
    correct_mark=forms.IntegerField(label='correct mark', required=True)
    negative_mark=forms.IntegerField(label='negative mark', required=True)
    

        
    
    