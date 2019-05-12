from django import forms
from .models import AuthUser

class RegistrationForm(forms.ModelForm):

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    
    class Meta:
       model = AuthUser
       fields = ('email', 'first_name', 'last_name', )

    def signup(self, request, user):
          first_name =  self.cleaned_data['first_name']
          last_name = self.cleaned_data['last_name']
          person = AuthUser(username=request.user.username, first_name=first_name, last_name=last_name, is_superuser=False, is_staff=False)
          person.save()