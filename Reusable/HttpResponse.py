from django.http import HttpResponse
from rest_framework.response import Response


#For this to work, must inherit the HttpResponse class otherwise
'''
THis not work right now 
'''
def returnResponse(request, msg, code):
    print("Come here")
    return HttpResponse(msg, status =code)

# class genericResponse(HttpResponse):

