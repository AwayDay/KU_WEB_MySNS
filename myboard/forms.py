# make sure this is at the top if it isn't already
from django import forms
from models import webSNS

# our new form
class PostForm(forms.ModelForm):
    class Meta:
        model = webSNS
        fields = ('password', 'content',)
'''
        password = forms.CharField(required=True)
        content = forms.CharField(
            required=True,
            widget=forms.Textarea
        )
'''
