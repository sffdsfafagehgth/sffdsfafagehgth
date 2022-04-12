from django.shortcuts import render



def index(request):
    return render(request, 'main/base.html',)

def aboba(request):
    return render(request, 'main/22.html',)
def lox(request):
    return render(request, 'main/lox.html',)


