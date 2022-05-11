from django import forms
from lists.models import Item

EMPTY_ITEM_ERROR = "You can't have an empty list item"


class ItemForm(forms.Form):
    _error_messages = {
            'text': {'required': EMPTY_ITEM_ERROR}
    }
    text = forms.CharField(required=True, max_length=256, error_messages=_error_messages['text'])

    class Meta:
        model = Item
        fields = ('text',)
        widgets = {
            'text': forms.fields.TextInput(attrs={
                'placeholder': 'You are welcome !!!',
                'class': 'form-control input-lg',
            }),
        }
