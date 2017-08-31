# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	lastest_question_list = Question.objects.order_by('-pub_date')[:5]
	output = ', '.join([q.question_text for q in lastest_question_list])
	return HttpResponse(ouput)

def detail(request, question_id):
	return HttpResponse("You're looking at question %s" %question_id)

def results(request, question_id):
	response = "You're looking at the results of questions %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)
