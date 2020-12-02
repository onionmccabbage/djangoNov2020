from django import forms # Django form widgets are now available

class NameForm(forms.Form):
    user_name = forms.CharField(label='Enter Your Name', max_length=64)
    subject = forms.CharField(label='Subject', max_length=120)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False) 