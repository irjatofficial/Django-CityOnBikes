from django import forms
from .models import BookingDetails
from django.forms.widgets import SelectDateWidget
from datetime import datetime
from django.contrib.admin import widgets



class BookingForm(forms.ModelForm):
    now = datetime.now()
    BookingDetails.destination = forms.SlugField(required=True)
    BookingDetails.pickup_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M:%S'))
    BookingDetails.return_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M:%S'))
    #Meta is Used to Config Models And Fieldssssssssssssss.......

    class Meta:
        model = BookingDetails
        fields = ['destination','pickup_time','return_time']

