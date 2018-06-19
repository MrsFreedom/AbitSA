
from django.shortcuts import render

def km(request):
    return render(request, 'blog/km.html')
def sapr(request):
    return render(request, 'blog/sapr.html')
def sa(request):
    return render(request, 'blog/sa.html')
def aphp(request):
    return render(request, 'blog/aphp.html')
def main(request):
    return render(request, 'blog/main.html')

def base(request):
    return render(request, 'blog/base.html')
def magistr(request):
    return render(request, 'blog/magistr.html')
def bacalavr(request):
    return render(request, 'blog/bacalavr.html')

def dostijenia(request):
    return render(request, 'blog/dostijenia.html')
def table(request):
    return render(request, 'blog/table.html')


