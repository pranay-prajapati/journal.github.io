from django import forms
from .models import JournalModel

class formName(forms.ModelForm):
    pass

    class Meta:
        model = JournalModel

        fields = '__all__'
