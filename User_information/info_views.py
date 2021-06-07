from django.shortcuts import render, redirect
from . import models, forms, form2
import hashlib  # 密码加密


def hash_code(s, salt='mysite'):  # 密码加密
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


# 用户查看个人信息
def info(request):
    if not request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/user/user_home/')
    # 获取当前用户名
    user_id = request.session['user_id']
    # print(user_id)

    # 创建具体用户对象：user
    user = models.User.objects.get(pk=user_id)

    # 返回一个 QuerySet 对象 ，包含所有的表记录
    # qs = user.values()

    return render(request, 'my_info/info.html', {"user": user})


# 用户职业期待添加和显示
def await_job(request):
    user_id = request.session['user_id']
    # print(user_id)#ok

    #  获取用户社对象
    user_await = models.User.objects.filter(pk=user_id).first()

    if request.method == 'POST':
        await_job_Form = form2.AwaitJobForm(request.POST)
        # 获取当前用户名

        # 实例化
        await_job_Form.is_valid()
        # 解决：AttributeError: 'form' object has no attribute 'cleaned_data'

        type = await_job_Form.cleaned_data.get('type')
        city = await_job_Form.cleaned_data.get('city')
        major = await_job_Form.cleaned_data.get('major')
        position = await_job_Form.cleaned_data.get('position')

        #print(type)#ok
        #print(city)
        #print(major)
        #print(position)

        # 创建用户的职业期待
        show_awa = models.Await.objects.create(
            # 用户外键
            user_await=user_await,
            type=type,
            city=city,
            major=major,
            position=position
        )
        awa = models.Await.objects.filter(user_await=user_await)
        return render(request, 'my_info/await_job.html', locals())

    # 获取用户期待名单
    awa = models.Await.objects.filter(user_await=user_await)
    await_job_Form = form2.AwaitJobForm()
    return render(request, 'my_info/await_job.html', locals())


# 修改用户信息
def alter_info(request):
    if not request.session.get('is_login', None):
        return redirect('/user/user_home/')

    if request.method == 'POST':
        alter_info_form = form2.AlterInfoForm(request.POST)
        # 获取当前用户名
        user_id = request.session['user_id']
        cur_user = models.User.objects.get(pk=user_id)
        #print(cur_user.name)#ok
        if not alter_info_form.is_valid():
            message = "无内容修改！"
            return render(request, 'my_info/alter_info.html', locals())

        username = alter_info_form.cleaned_data.get('username')
        if username:
            cur_user.name = username

        email = alter_info_form.cleaned_data.get('email')
        if email:
            cur_user.email = email

        phone = alter_info_form.cleaned_data.get('phone')
        if phone:
            cur_user.phone = phone

        edu = alter_info_form.cleaned_data.get('edu')
        if edu:
            cur_user.edu = edu

        major = alter_info_form.cleaned_data.get('major')
        if major:
            cur_user.major = major

        sex = alter_info_form.cleaned_data.get('sex')
        if sex:
            cur_user.sex = sex

        title = alter_info_form.cleaned_data.get('title')
        if title:
            cur_user.title = title

        skill = alter_info_form.cleaned_data.get('skill')
        if skill:
            cur_user.skill = skill

        exp = alter_info_form.cleaned_data.get('exp')
        if exp:
            cur_user.exp = exp

        address = alter_info_form.cleaned_data.get('address')
        if address:
            cur_user.address = address

        cur_user.save()
        message = "修改成功！"
        return redirect('/user/info/')

    alter_info_form = form2.AlterInfoForm()
    return render(request, 'my_info/alter_info.html', locals())


# 修改用户密码
def alter_pwd(request):
    if request.method == 'POST':
        alter_pwd_form = forms.alter_pwd_Form(request.POST)
        message = "请检查填写的内容！"
        if alter_pwd_form.is_valid():
            old_pwd = alter_pwd_form.cleaned_data.get('old_pwd')
            new_pwd = alter_pwd_form.cleaned_data.get('new_pwd')
            re_new_pwd = alter_pwd_form.cleaned_data.get('re_new_pwd')

            # 获取当前用户名
            user_name = request.session['user_name']

            # print(user_name)# check OK
            try:
                user = models.User.objects.get(name=user_name)
            except:
                message = '当前用户不存在！'
                return render(request, 'my_info/alter_pwd.html', locals())

            # print(user.pwd)# check OK
            # print(old_pwd)
            # print(hash_code(old_pwd))

            if user.pwd != hash_code(old_pwd):  # 验证旧密码是否正确
                message = '旧密码错误！'
                return render(request, 'my_info/alter_pwd.html', locals())

            if new_pwd != re_new_pwd:
                message = '两次输入的密码不同！'
                return render(request, 'my_info/alter_pwd.html', locals())
            else:
                message = '修改成功！'
                # print(hash_code(new_pwd))#数据ok
                user.pwd = hash_code(new_pwd)  # 加密修改密码
                user.save()
                # print(user.pwd)#ok
                return redirect('/user/user_home/')
        else:
            return render(request, 'my_info/alter_pwd.html', locals())
    alter_pwd_form = forms.alter_pwd_Form()
    return render(request, 'my_info/alter_pwd.html', locals())
