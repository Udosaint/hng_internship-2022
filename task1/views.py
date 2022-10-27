from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.

data = [
    {"slackUsername": "Udosaint", "backend": True, "age": 26, "bio": 'Hi am a fullstack developer and also a Data Analyst, Happy to meet you all'}
]


def Index(request):
    context = {'data': data}
    return HttpResponse(data)
