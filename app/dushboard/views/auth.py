#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from django.views.generic import View
from django.shortcuts import redirect,reverse
from app.libs.base_render import render_to_response
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from app.utils.permission import dushboard_auth


class Login(View):
    TEMPLATE ='dushboard/auth/login.html'
    def get(self,request):
        if request.user.is_authenticated:
            return redirect(reverse('dushboard_index'))
        to = request.GET.get('to','')
        data ={'error':'','to':to}
        return render_to_response(request, self.TEMPLATE,data=data)
    def post(self,request):
         username = request.POST.get("username")
         password = request.POST.get("password")
         exists = User.objects.filter(username=username).exists()
         to = request.GET.get('to', '')
         data ={}
         if not exists:
             data['error'] ='用户不存在'
             return render_to_response(request,self.TEMPLATE,data)
         user = authenticate(username=username,password=password)
         if not user:
             data['error'] = '密码错误'
             return render_to_response(request, self.TEMPLATE, data=data)
         if not user.is_superuser:
             data['error'] = '无权登录'
             return render_to_response(request, self.TEMPLATE, data=data)
         login(request,user)
         if to:
             print(to)
             return redirect(to)
         return redirect(reverse('dushboard_index'))
         # pass
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('dushboard_login'))
class AdminManage(View):
    TEMPLATE = 'dushboard/auth/admin.html'
    @dushboard_auth
    def get(self, request):
        user = User.objects.all()
        page = request.GET.get('page', 1)
        p = Paginator(user,2)
        total_page =p.num_pages
        if int(page) <1:
            page =1
        current_page = p.get_page(int(page)).object_list
        data ={'Users':current_page,'total':total_page,'page_num':int(page)}
        print(data)
        return render_to_response(request, self.TEMPLATE,data=data)
class UpdateAdminStatus(View):
    def get(self, request):
        status = request.GET.get('status')
        _status = True if status=='on' else False
        request.user.is_superuser =_status
        request.user.save()
        return redirect(reverse('dushboard_admin'))