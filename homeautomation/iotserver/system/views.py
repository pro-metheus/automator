from django.http import HttpResponse
# Create your views here.
from .models import Device
import json


def modifer(request,key,state):
    try:
        device=Device.objects.get(uid=key)
        if state=='1' or state =='0':
            device.state=state
            device.save()
            alert=False
        else:
            alert=True
        if not alert:
            confirm={'accepted':'True'}
            return HttpResponse(json.dumps(confirm))
        else:
            confirm={'accepted':'False'}
            return HttpResponse(json.dumps(confirm))
    except:
        confirm = {'accepted': 'False'}
        return HttpResponse(json.dumps(confirm))

def stream(request,key):
    device = Device.objects.get(uid=key)
    data={}
    data['name']=device.name
    data['pin']=device.pin
    data['state']=device.state
    cab=json.dumps(data)
    return HttpResponse(cab)
