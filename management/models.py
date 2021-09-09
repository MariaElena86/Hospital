from django.db import models
import uuid
# Create your models here.


class Specialty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ailment(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Patient(models.Model):
    # Fields
    name = models.CharField(max_length=20, help_text='Enter the name of patient')
    ailment = models.ForeignKey(Ailment, on_delete=models.CASCADE, help_text='Enter the ailment of patient')

    def __str__(self):
        return self.name

    # Metadata
    class Meta:
        ordering = ['-name']


class Doctor(models.Model):
    # Fields
    name = models.TextField(max_length=255, null=False)
    speciality = models.ForeignKey(Specialty, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    # Metadata
    class Meta:
        ordering = ['-name']


class Review(models.Model):
    # Fields
    EMPATHY_CHOICES = (
        (0, 'Low'),
        (1, 'Medium'),
        (2, 'High')
    )

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, db_column='doctor_pk', related_name='reviews')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, db_column='patient_pk', related_name='reviews')
    description = models.TextField(max_length=255, null=False)
    empathy = models.IntegerField(null=False, default=0, choices=EMPATHY_CHOICES)
    personal = models.IntegerField(null=False, default=0, choices=EMPATHY_CHOICES, verbose_name='Personal Values')

    def __str__(self):
        return self.doctor.name


class Match(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, db_column='patient_pk', related_name='match')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, db_column='doctor_pk', related_name='match')

