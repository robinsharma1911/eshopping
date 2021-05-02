from django import forms

class RegisterForm(forms.Form):
    first_name = forms.CharField(label='First name',max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last name',max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email',max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Phone',max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password',max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email',max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password',max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))