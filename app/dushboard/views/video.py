#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from django.views.generic import View
from django.shortcuts import redirect,reverse
from app.libs.base_render import render_to_response
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from app.utils.permission import dushboard_auth

class ExternaVideo(View):
    TEMPLATE = 'dushboard/video/externa_video.html'
    @dushboard_auth
    def get(self,request):
        return render_to_response(request, self.TEMPLATE)