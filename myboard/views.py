from django.shortcuts import render
from django.shortcuts import render_to_response
from myboard import models
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from .forms import PostForm

# Create your views here.

def SnsView(request, idx):
    docs = models.webSNS.objects.all()

    if idx:
        print('id')
        doc = models.webSNS.objects.get(id = idx)
        print(doc.content)
        #doc.delete()
        form = PostForm()
        return render(request, 'timeline.html', {'form': form, 'docs' : docs})
    else:
        if request.method == 'POST':
            print('POST')
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
