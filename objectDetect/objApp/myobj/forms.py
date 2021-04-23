from django import forms

class objectDetect(forms.Form):
    imgfile = forms.ImageField()
    xmlfile = forms.FileField()

class getReport(forms.Form):
    startdate = forms.DateField()
    enddate = forms.DateField()