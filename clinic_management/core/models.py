from django.db import models

# Patient Model
class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Doctor Model
class Doctor(models.Model):
    name = models.CharField(max_length=200)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

# Medicine Model
class Medicine(models.Model):
    name = models.CharField(max_length=200)
    batch_number = models.CharField(max_length=100, unique=True)
    expiry_date = models.DateField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    manufacturer = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Appointment Model
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()

    def __str__(self):
        return f"Appointment for {self.patient} with {self.doctor} on {self.date}"
