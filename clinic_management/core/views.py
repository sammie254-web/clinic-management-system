from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import Medicine
from .forms import MedicineForm
from .models import Patient
from .forms import PatientForm
from .models import Doctor
from .forms import DoctorForm
from .models import Appointment
from .forms import AppointmentForm

def appointments_list(request):
    appointments = Appointment.objects.select_related('patient', 'doctor').all()
    return render(request, 'core/appointments_list.html', {'appointments': appointments}) 

def add_appointment(request):
    patients = Patient.objects.all()  
    doctors = Doctor.objects.all()  

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointments_list')
        else:
            print(form.errors)  
    else:
        form = AppointmentForm()

    return render(request, 'core/appointment_form.html', {
        'form': form, 
        'action': 'add',
        'patients': patients,  
        'doctors': doctors,  
    })
    

def edit_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointments_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'core/appointment_form.html', {'form': form, 'action': 'edit', 'appointment': appointment})

def delete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.delete()
    return redirect('appointments_list')

def doctors_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'core/doctors_list.html', {'doctors': doctors})

def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctors_list')
    else:
        form = DoctorForm()
    return render(request, 'core/doctor_form.html', {'form': form, 'action': 'add'})

def edit_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctors_list')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'core/doctor_form.html', {'form': form, 'action': 'edit', 'doctor': doctor})

def delete_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    doctor.delete()
    return redirect('doctors_list')

def patients_list(request):
    patients = Patient.objects.all()
    return render(request, 'core/patients_list.html', {'patients': patients})

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patients_list')
    else:
        form = PatientForm()
    return render(request, 'core/patient_form.html', {'form': form, 'action': 'add'})

def edit_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patients_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'core/patient_form.html', {'form': form, 'action': 'edit', 'patient': patient})

def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    patient.delete()
    return redirect('patients_list')

def medicines_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'core/medicines_list.html', {'medicines': medicines})

def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicines_list')
    else:
        form = MedicineForm()
    return render(request, 'core/medicine_form.html', {'form': form, 'action': 'add'})

def edit_medicine(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('medicines_list')
    else:
        form = MedicineForm(instance=medicine)
    return render(request, 'core/medicine_form.html', {'form': form, 'action': 'edit', 'medicine': medicine})

def delete_medicine(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    medicine.delete()
    return redirect('medicines_list')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('login') 
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('home') 
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'core/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')  


def home(request):
    return render(request, 'core/home.html')
