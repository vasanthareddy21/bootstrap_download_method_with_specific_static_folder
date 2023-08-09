from django.shortcuts import render

# Create your views here.
def bootstrap_download(request):
    return render(request,'bootstrap_download.html')

def pagination(request):
    return render(request,'pagination.html')

def spinners(request):
    return render(request,'spinners.html')

def forms(request):
    return render(request,'forms.html')

def progress(request):
    return render(request,'progress.html')

def inputgroup(request):
    return render(request,'inputgroup.html')

def scrollspy(request):
    return render(request,'scrollspy.html')

def toasts(request):
    return render(request,'toasts.html')

def mediaobject(request):
    return render(request,'mediaobject.html')

def navs(request):
    return render(request,'navs.html')
