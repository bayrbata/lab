from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render
from datetime import datetime
import json

# Create your views here.
def current_time(request):
    return HttpResponse(datetime.now())

def checkService(request):
    if request.method == "POST":

    else:
        result = sendResponse(request, 3002, [], "not POST method")
        return JsonResponse(json.loads(result))
    
def sendResponse(request, resultCode, data, action = "no action " ):
    response = {}
    response["resultCode"] = resultCode
    response["resultMessage"] = resultMessages[resultCode]
    response[""] = {}
    response = {}
    response = {}
    response = {}
