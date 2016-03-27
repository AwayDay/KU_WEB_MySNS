# make sure this is at the top if it isn't already
from django import forms

# our new form
class PostForm(forms.Form):
    password = forms.CharField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
