#-*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render_to_response, RequestContext
from myboard import models
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from .forms import PostForm

from django.core import serializers
from django.core.paginator import Paginator
import json

# Create your views here.

def SnsView(request, idx):
    docs = models.webSNS.objects.all().reverse()
    #print(type(docs))
    #print(docs.reverse())
    PDocs = Paginator(docs, 15)

    if request.method == 'POST':

        if 'post' in request.POST:
            print('post, wow!')
            form = PostForm(request.POST)
            if form.is_valid():
                print(request.POST['password'])
                print(request.POST['content'])
                form.save()
                form = PostForm()
                return render(request, 'timeline.html', {'form': form, 'docs' : PDocs.page(1)})
                #return render(request, 'timeline.html', {'form': form, 'docs' : docs})
            else:
                form = PostForm()
                return render(request, 'timeline.html', {'form': form, 'docs' : PDocs.page(1)})
                #return render(request, 'timeline.html', {'form': form, 'docs' : docs})

        elif 'delete' in request.POST:
            print('delete, nice!')
            form = PostForm()
            if idx:
                print('idx OK')
                doc = models.webSNS.objects.get(id = idx)
                return render(request, 'del.html', {'form': form, 'doc' : doc})
            else:
                print('somthing is wrong')
                return render(request, 'timeline.html', {'form': form, 'docs' : PDocs.page(1)})
                #return render(request, 'timeline.html', {'form': form, 'docs' : docs})

        elif 'del' in request.POST:
            print('DELETE')
            if idx:
                print('idx OK')
                if request.POST.get('del_password'):
                    print(request.POST.get('del_password'))
                    doc = models.webSNS.objects.get(id = idx)
                    if doc.password == request.POST.get('del_password'):
                        print('correct!')
                        doc.delete()
                    else:
                        print('nonono')
            else:
                print('somthing is wrong')
            form = PostForm()
            return render(request, 'timeline.html', {'form': form, 'docs' : PDocs.page(1)})
            #return render(request, 'timeline.html', {'form': form, 'docs' : docs})

        elif request.is_ajax():
            print('AJAX POST test')
            page = int(request.POST.get('NumPage'))
            #print("page: ",page)
            if page <= PDocs.num_pages:
                #print(PDocs.page(page).object_list)
                data = serializers.serialize("json", PDocs.page(page).object_list)
                return HttpResponse(data, content_type='application/json')
                #return render(request, 'timeline.html', {'form': form, 'docs' : tmpdoc})
            else:
                print('fali')
            form = PostForm()
            return render(request, 'timeline.html', {'form': form, 'docs' : PDocs.page(1)})
            #return render(request, 'timeline.html', {'form': form, 'docs' : docs})

        else:
            print('??')
            form = PostForm()
            return render(request, 'timeline.html', {'form': form, 'docs' : PDocs.page(1)})
            #return render(request, 'timeline.html', {'form': form, 'docs' : docs})

    else:
        form = PostForm()
        return render(request, 'timeline.html', {'form': form, 'docs' : PDocs.page(1)})
        #return render(request, 'timeline.html', {'form': form, 'docs' : docs})
