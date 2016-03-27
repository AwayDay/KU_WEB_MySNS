from django.shortcuts import render
from django.shortcuts import render_to_response
from myboard import models
# Create your views here.

def board_view(request, urlCode, idx):
    boards = models.webBoard.objects.all()

    if urlCode:
        if idx:
            doc = models.webDoc.objects.get(board__urlCode = urlCode, id = idx)
            return render_to_response('detail.html', {'boards':boards, 'doc' : doc})
        else:
            docs = models.webDoc.objects.filter(board__urlCode = urlCode)
            return render_to_response('boards.html', {'boards':boards, 'docs' : docs})
    else:
        return render_to_response('index.html', {'boards':boards})
