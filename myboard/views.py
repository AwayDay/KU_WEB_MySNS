from django.shortcuts import render
from django.shortcuts import render_to_response
from myboard import models
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from .forms import PostForm

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
    docs = models.webSNS.objects.all()
    #docs = models.webDoc.objects.filter()
    #docs = models.webSNS.objects.filter()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            print(request.POST['password'])
            print(request.POST['content'])
            form.save()
            form = PostForm()
            return render(request, 'timeline.html', {'form': form, 'docs' : docs})
        else:
            form = PostForm()
            return render(request, 'timeline.html', {'form': form, 'docs' : docs})
    else:
        form = PostForm()
        return render(request, 'timeline.html', {'form': form, 'docs' : docs})
