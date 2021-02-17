from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    #
    return render(request, )

def blog(request):
    return HttpResponse("This is my blog page created by Juwana (/blog)")
