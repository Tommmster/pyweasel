from django.http import HttpResponse
from django.shortcuts import render_to_response

def choose_interview(request):
	return render_to_response("existing_interviews.html",{'question_sets':["JavaSr", "JavaCore", "Python"]})

def interview(request,name=None):

	if (name is None):
		return HttpResponse("This should not happen, should it? Stick to the menu options")

	return render_to_response('interview.html',{'name':name})
	

