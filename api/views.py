from django.shortcuts import render, redirect
from .forms import QuestionForm
from django.http import HttpResponseRedirect
import requests
import json
from .models import Question


def home(request):
	base_url='https://api.stackexchange.com/2.3/search/advanced'
	form=QuestionForm()
	if request.method=="POST":
		form=QuestionForm(request.POST)
		if form.is_valid():
			title=request.POST.get('title')
			page=request.POST.get("page")
			site=request.POST.get('site')
			order=request.POST.get('order')
			sort=request.POST.get('sort')
			closed=request.POST.get('closed')
			notice=request.POST.get('notice')
			wiki=request.POST.get('wiki')
			migrated=request.POST.get('migrated')
			accepted=request.POST.get('accepted')
			payload={
					"title":title,"page":page,
					"site":site,"order":order,
					"sort":sort,"closed":closed,
					"notice":notice,"wiki":wiki,
					"accepted":accepted,"migrated":migrated
					}
			response=requests.get(base_url,params=payload)
			resp=response.json()
			r=resp['items'][0]
			question_url=r['link']
			return render(request,'api/about.html',{"question_url":question_url})
	context={"form":form}
	return render(request,'api/home.html',context)