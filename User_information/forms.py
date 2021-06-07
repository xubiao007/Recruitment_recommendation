from django import forms
from captcha.fields import CaptchaField # 验证码包


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Username", 'autofocus': ''}))
    password = forms.CharField(label="密码", max_length=20, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': "Password"}))
    captcha = CaptchaField(label='验证码')

    '''    
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Username", 'autofocus': ''}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': "Password"}))
    '''


class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(label="用户名", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='电话号', max_length=11, widget=forms.TextInput(attrs={'class': 'form-control'}))
    edu = forms.CharField(label='学历', max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    major = forms.CharField(label='专业', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    pwd1 = forms.CharField(label="密码",min_length=5, max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    pwd2 = forms.CharField(label="确认密码", max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')


class alter_pwd_Form(forms.Form):
    old_pwd = forms.CharField(label="旧密码", max_length=20, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': "Old password"}))
    new_pwd = forms.CharField(label="新密码",min_length=5, max_length=20, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': "New password"}))
    re_new_pwd = forms.CharField(label="重新确认新密码", max_length=20, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': "Reconfirm new password"}))
    captcha = CaptchaField(label='验证码')





