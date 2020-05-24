#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import hashlib
from django.db import models

def has_password(password):
    if isinstance(password,str):
        password = password.encode('utf-8')
    return hashlib.md5(password).hexdigest().upper()

class ClentUser(models.Model):
    username = models.CharField(max_length=50,null=False,unique=True)
    password = models.CharField(max_length=255,null=False)
    avatar =models.CharField(max_length=500,default='')
    gender =models.CharField(max_length=10,default='')
    birthday =models.DateTimeField(null=True,blank=True,default=None)
    status =models.BooleanField(default=True,db_index=True)
    createtime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 'username:{}'.format(self.username)
    @classmethod
    def add(cls,username,password,avatar='',gender='',birthday=None):
        return cls.objects.create(
            username =username,
            password =has_password(password),
            avatar =avatar,
            gender=gender,
            birthday =birthday,
            status= True
        )
    @classmethod
    def get(cls,username,password):
        try:
            user = cls.objects.get(username=username,password=password)
            return  user
        except:
            return  None
    def updatepassword(self,oldpassword,newpassword):
        has_old_password = has_password(oldpassword)
        if has_old_password != self.password:
            return  False
        has_new_password = has_password(newpassword)
        self.password = has_new_password
        self.save()
        return True
    def updatestatus(self):
        self.status = not self.status
        self.save()
        return  True
