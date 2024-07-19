from django import forms

class StudForm(forms.Form):
    s_name=forms.CharField(max_length=50,label='Student Name')
    s_class=forms.CharField(max_length=50,label='Class')
    s_addr=forms.CharField(max_length=50,label='Address')
    s_school=forms.CharField(max_length=50,label='School Name')
    s_email=forms.EmailField(max_length=50,label='Student E-mail')

class SForm(forms.Form):
    s_name=forms.CharField(max_length=50,label='Student name')