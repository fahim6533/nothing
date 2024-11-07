from django import forms 
from user_profile_app.models import User



class user_login_form(forms.Form):
    username= forms.CharField(max_length=20,required=True)
    password=  forms.CharField(max_length=100,required=True, widget=forms.PasswordInput)









class User_registration_form(forms.ModelForm):

    class Meta:
        model= User
        fields= ["username","email","password"]

    # def clean_username(self):
    #     username= self.cleaned_data.get('username')
    #     model=self.Meta.model
    #     user = model.objects.filter(username__iexact=username)
    #     if user.exists():
    #         raise forms.ValidationError("This user is already exists")
        
    #     return self.cleaned_data.get('username')
        
        

    # def clean_email(self):
    #     email= self.cleaned_data.get('email')
    #     model=self.Meta.model
    #     user= model.objects.filter(email__iexact=email)
    #     if user.exists():
    #         raise forms.ValidationError("This email is already exists")
        
    #     return self.cleaned_data.get('email')
        

    # def clean_password(self):
    #     password= self.cleaned_data.get('password')
    #     confirm_password=self.data.get('confirm_password')

    #     if password != confirm_password:
    #         raise forms.ValidationError("Password do not match")
    #     return self.cleaned_data.get('password')


class user_profile_update(forms.ModelForm):
    def _init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
    class Meta:
        model= User
        fields= ["first_name","last_name","username","email"]
    
    # def clean_username(self):
    #     username=self.cleaned_data.get('username')
    #     model=self.Meta.model
    #     user = model.objects.filter(username__iexact=username).exclude(pk=self.instance.pk)
    #     if user.exists():
    #         raise forms.ValidationError("This user is already exists")
        
    #     return self.cleaned_data.get('username')
        
        

    # def clean_email(self):
    #     email= self.cleaned_data.get('email')
    #     model=self.Meta.model
    #     user= model.objects.filter(email__iexact=email).exclude(pk=self.instance.pk)
    #     if user.exists():
    #         raise forms.ValidationError("This email is already exists")
        
    #     return self.cleaned_data.get('email')
        

    # def clean_password(self):
    #     password= self.cleaned_data.get('password')
    #     confirm_password=self.data.get('confirm_password')

    #     if password != confirm_password:
    #         raise forms.ValidationError("Password do not match")
    #     return self.cleaned_data.get('password')


    def change_password(self):
        if 'new password' in self.data and 'confirm_password' in self.data:
            new_password=self.data['new_password']
            confirm_password=self.data['confirm_password']
            if new_password != '' and confirm_password != '':
                if new_password != confirm_password:
                    raise forms.ValidationError("Passwords don't match")
                else:
                    self.isinstance.set_password(new_password)
                    self.instance.save()
    def clean(self):
        self.change_password()


class profile_picture_update(forms.Form):
    profile_picture=forms.ImageField(required=True)