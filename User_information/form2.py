from django import forms


# 添加用户“职业期待”的表单
class AwaitJobForm(forms.Form):
    a = (
        ('bux', '不限'),
        ('quan', '全职'),
        ('jian', '兼职'),
        ('shix', '实习'),
)
    type = forms.ChoiceField(choices=a, label='职业类型')
    city = forms.CharField(max_length=10, label='期待城市',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    major = forms.CharField(max_length=16, required=False, label='专业方向',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    position = forms.CharField(max_length=20, required=False, label='职位名称',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))




class AlterInfoForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    username = forms.CharField(label="用户名", required=False, max_length=20,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", required=False,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='电话号', required=False, max_length=11,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    edu = forms.CharField(label='学历', required=False, max_length=10,
                          widget=forms.TextInput(attrs={'class': 'form-control'}))
    major = forms.CharField(label='专业', required=False, max_length=20,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', required=False, choices=gender)
    title = forms.CharField(max_length=20, required=False, label='职称',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    skill = forms.CharField(max_length=20, required=False, label='技能',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    exp = forms.CharField(max_length=20, required=False, label='经验',
                          widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=60, required=False, label='地址',
                              widget=forms.TextInput(attrs={'class': 'form-control'}))



