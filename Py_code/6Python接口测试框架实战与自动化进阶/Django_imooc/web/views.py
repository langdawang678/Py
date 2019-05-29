'''
3-2 django之接口工作原理.mp4
from django.http.response import HttpResponse
# Create your views here.
def Login(request):
    return HttpResponse('this is first test')
'''
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http.response import HttpResponse
from django.shortcuts import render_to_response

import json

# Create your views here.
def Login(request):
    if request.method == "POST":
        result ={}
        username = request.POST.get('username')
        mobile = request.POST.get('password')
        #data = request.GET.get('data')
        result['user'] = username
        result['mobileNumber'] = mobile
        #result['data'] = data
        result =json.dumps(result)
        return HttpResponse(result,content_type='application/json;charset=utf-8')
    else:
        return render_to_response('login.html')
