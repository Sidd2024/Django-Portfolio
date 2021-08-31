from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView
from .models import Contact
from django.urls import reverse_lazy
from .forms import ContactForm
from .models import Contact
from .models import Post
from django.views.generic import DetailView
from django.views.generic import ListView
from django.utils import timezone


# from django.core.mail import send_mail, BadHeaderError, EmailMessage

# Create your views here.
def home(request):
    # context = {'name': 'Juwana', 'Portfolio': 'Django'}
    return render(request, 'home.html')

class ContactCreate(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy("thanks")


def thanks(request):
    return HttpResponse("Thank you! Will get in touch soon.")


def contact(request):
    if request.method=="POST":
        # form = ContactForm(data=request.POST)
        # if form.is_valid():
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        #print(name, email, message)
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        print("The data has been written to the db")

        # Email the profile with the contact information
    #         send_mail(name, message, email, ['testmail@gmail.com'], fail_silently=False)

        #return HttpResponseRedirect('/contact')
    # else:
    #     form = ContactForm()


    return render(request, 'contact.html')


class PostList(ListView):
    ordering = ['created_on']
    template_name = 'blog.html'
    context_object_name = 'posts'
    model = Post

class PostDetail(DetailView):
    model = Post
    ordering = ['created_on']
    template_name = 'post_detail.html' #'post_detail.html'
    
# def blog(request):

#     posts = Post.objects.all()
#     context = {'posts': posts}
#     return render(request, 'blog.html', context)
