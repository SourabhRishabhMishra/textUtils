# I have created this file - sourabh mishra
from django.http import HttpResponse
from django.shortcuts import render
import re

def index(request):
    return render(request,'index.html')
    #return HttpResponse("Home")

def analyze(request):
    #get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    print(djtext)
    print(removepunc)
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params={'purpose':'Removed Punctuation','Analyzed_text':'' + analyzed}
        djtext = analyzed
        #analyse the text
        #return render(request,'analyze.html',params)
    if fullcaps == "on":
        analyzed=''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params={'purpose':'Removed Punctuation','Analyzed_text':'' + analyzed}
        #analyse the text
        djtext = analyzed
        #return render(request,'analyze.html',params)
    if newlineremover == "on":
        analyzed=''
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Removed Punctuation', 'Analyzed_text': '' + analyzed}
        # analyse the text
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if extraspaceremover == "on":
        analyzed=''
        for  char in djtext:
            analyzed = re.sub(' +', ' ', djtext)
        params = {'purpose': 'Removed Punctuation', 'Analyzed_text': '' + analyzed}
        # analyse the text
        #return render(request, 'analyze.html', params)
    if(removepunc != "on" and newlineremover !="on" and extraspaceremover!="on" and fullcaps !="no" ):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)
# def capitalizefirst(request):
#     return HttpResponse("capitalize first ")
#
# def newlineremove(request):
#     return HttpResponse("newlineremove")
#
# def spaceremove(request):
#     return HttpResponse("spaceremove <a href='/'>Back</a>")
#
# def charcount(request):
#     return HttpResponse("charcount")
