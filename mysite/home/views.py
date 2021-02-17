from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # context = {'name': 'Juwana', 'Portfolio': 'Django'}
    return render(request, 'home.html')

def blog(request):
    # return HttpResponse("This is my blog page created by Juwana (/blog)")
    return render(request, 'blog.html')
