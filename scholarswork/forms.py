from django import forms
# from .models import Coursefiles
from django.shortcuts import get_object_or_404


YEARS = (
    ("2014/2015","2014/2015"),
    ("2015/2016","2015/2016"),
    ("2016/2017","2016/2017"),
    ("2017/2018","2017/2018"),
)

class CourseDownloadForm(forms.Form):
    year = forms.MultipleChoiceField(choices=YEARS)

