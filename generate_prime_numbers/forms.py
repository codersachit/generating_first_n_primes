from django import forms

class InputFormForN(forms.Form):
   n = forms.CharField(required=True)

class InputFormForRequestId(forms.Form):
    request_id = forms.CharField(required=True)