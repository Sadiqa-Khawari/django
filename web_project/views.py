# from django.http import HttpResponse


#def Koti(request):
    #return HttpResponse("Hei Mailma")



from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
 
# Create your views here.
def Koti(request):
    return HttpResponse("HEI MAAILMA!, Tervetuloa Djangoon! Tänään on " + str(datetime.now()))



