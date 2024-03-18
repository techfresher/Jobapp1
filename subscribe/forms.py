from django import forms
from subscribe.models import Subscribe
from django.utils.translation import gettext_lazy as _

class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields = "__all__"

        labels = {
            'first_name':_('Enter First Name'),
            'last_name':_('Enter Last Name'),
            'email':_('Enter Email')
        }
        error_messages = {
            'first_name':{
                'required':_('first name is required')
            }
        }



