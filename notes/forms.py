from django import forms
from django.core.exceptions import ValidationError

from . models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ("title", "text")
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control my-5'}),
            'title' : forms.Textarea(attrs={'class':'form-control mb-5'})
        }
        labels = {
            'text' : 'label text'
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError('We accept note about Django')

        return title