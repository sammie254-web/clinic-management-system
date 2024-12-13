from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Patient
from .models import Medicine
from .models import Doctor
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date is None:
            raise forms.ValidationError("Date is required.")
        
        from datetime import date as dt
        if date < dt.today():
            raise forms.ValidationError("The date cannot be in the past.")
        return date

    def clean_time(self):
        time = self.cleaned_data.get('time')
        if time is None:
            raise forms.ValidationError("Enter a valid time in HH:MM format.")
        return time

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        
        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
