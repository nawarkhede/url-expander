# Create your views here.
import requests
from django.shortcuts import render

def expand(request):
    shorturl=None
    if request.GET['textinput'] and len(request.GET['textinput']) < 30 :
        try:
            if request.GET['textinput'].startswith('http'):
                final=request.GET['textinput']
            else:
                final='http://'+request.GET['textinput']
            shorturl=requests.head(final).headers['location']
        except:
            shorturl='Error occured : url not valid'
            
    else:
        shorturl='Error occured : not a short url'
    return render(request, 'index.html', {"shorturl": shorturl})

def home(request):
    return render(request, 'index.html', {"foo": "bar"})
'''
def home(request):
    try:
        all_items = request.GET.getlist('url')
        response_data=[]
        for i in all_items:
            try:
                u=''
                if i.startswith('http'):
                    u=i
                else:
                    u='http://'+i
                data={'requested_url':i ,'long-url':requests.head(u).headers['location'],'success':'True'}
                response_data.append(data)
            except Exception as e:
                data={'requested_url':i ,'error':str(e).split(':')[0],'success':'False'}
                response_data.append(data)
        if not response_data:
            raise Exception('I Love Python :)')
            
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    except Exception as e:
        return HttpResponse("""
<h3>Welcome , you must supply the short url. </h3></br>
<i>e.g  http://longurlapi.appspot.com/?url=http://something.com/12345</i></br>
<i>Another e.g. http://longurlapi.appspot.com/?url=http://something.com/12345&url=http://something1.com/12345&url=http://something.com/12345... </i>
<hr>
Author : Nishant Nawarkhede<br>
Email  : nishant.nawarkhede@gmail.com
</br><hr>
"""+str(e))
'''