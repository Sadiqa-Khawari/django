# from django.http import HttpResponse


#def Koti(request):
    #return HttpResponse("Hei Mailma")



from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
 
# Create your views here.
def Koti(request):
    now = datetime.now().strftime("%H:%M:%S")
    context = {
        "tervehdysteksti": "Tervetuloa mailmaan!",
        "kelloaika": now,
    }
    return render(request, "web_project/testi.html", context)
    #return HttpResponse("HEI MAAILMA!, Tervetuloa Djangoon! Tänään on " + str(datetime.now()))



