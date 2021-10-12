from django.forms import ModelForm
from django.forms import Textarea, EmailField, CharField
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'message']
        widgets = {
            "message": Textarea(attrs={
                "placeholder": "Send me a message"
            })
        }