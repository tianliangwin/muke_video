#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import  functools
from django.shortcuts  import redirect,reverse

def dushboard_auth(fun):
    @functools.wraps(fun)
    def wrapper(self,request,*args,**kwargs):
        user =request.user
        if not user.is_authenticated  or not user.is_superuser:
            return redirect('{}?to={}'.format(reverse('dushboard_login'),request.path))
        return fun(self,request,*args,**kwargs)
    return wrapper