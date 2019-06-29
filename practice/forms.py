from django import forms

class postWriting(forms.Form):
    post_text = forms.CharField(label='', max_length=10000,
                                widget=forms.Textarea(attrs={'placeholder':'Write here!'}))

#class followUsers(forms.Form):
#    triedUsername = forms.CharField(label='', max_length=20)
    
class folUsers(forms.Form):
    tried_user = forms.CharField(label='', max_length=10000)
