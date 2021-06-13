from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView
from .models import Contact
from django.urls import reverse_lazy
from .forms import ContactForm
from home.models import Contact
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

def blog(request):
    # return HttpResponse("This is my blog page created by Juwana (/blog)")
    context = {'name': 'Juwana Zerman', 'phrase': 'What I Have Been Up To'}
    return render(request, 'blog.html', context)
