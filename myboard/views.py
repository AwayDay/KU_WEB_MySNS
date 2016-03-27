from django.shortcuts import render
from django.shortcuts import render_to_response
from myboard import models
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def board_view(request, urlCode, idx):
    boards = models.webSNS.objects.all()

    return render_to_response('index.html', {'boards':boards})

'''
    if urlCode:
        if idx:
            doc = models.webDoc.objects.get(board__urlCode = urlCode, id = idx)
            return render_to_response('detail.html', {'boards':boards, 'doc' : doc})
        else:
            docs = models.webDoc.objects.filter(board__urlCode = urlCode)
            return render_to_response('boards.html', {'boards':boards, 'docs' : docs})
    else:
        return render_to_response('index.html', {'boards':boards})
'''

def SnsView(request, idx):
    timline = models.webSNS.objects.all()
    if idx:
        return render_to_response('index.html', {'timline':timline})
    else:
        return render_to_response('index.html', {'timline':timline})

def SnsPost(request):
    c = {}
    c.update(csrf(request))
    #password = request.POST['password']
    #content = request.POST['content']
    #return HttpResponse(password + content)
    return render_to_response('boards.html', {'boards':boards, 'docs' : docs})
