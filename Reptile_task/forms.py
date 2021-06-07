from django import forms


# 输入职位关键词的form
class JobKeyForms(forms.Form):
    job_key = forms.CharField(label="职位关键词", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))


# 输入所需页数的form
class RequiredPageForms(forms.Form):
    requires_page = forms.IntegerField(min_value=0,max_value=9999)







