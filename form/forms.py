from django import forms

from .models import ConsignmentItem

class ConsignmentItemForm(forms.ModelForm):

    class Meta:
        model = ConsignmentItem
        # fields = ('title', 'text',)
