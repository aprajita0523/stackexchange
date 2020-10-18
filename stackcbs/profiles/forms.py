from django import forms
from .models import Profile

class ProfileModelForm(forms.ModelForm):
    class Meta:   #with this we indicate that we want to work with Profile Model
        model = Profile
        #we can do 

        fields = ('first_name','last_name','bio','avatar')
