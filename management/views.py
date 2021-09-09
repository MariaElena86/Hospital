from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from management.forms import *
from management.models import *


class MatchView(FormView):
    template_name = 'match.html'
    form_class = MatchForm

    def form_valid(self, form):
        print('doctor selected')
        patient = Patient.objects.get(pk=form.data['patient'])
        doctors = Doctor.objects.filter(speciality=patient.ailment.specialty)
        if Review.objects.filter(doctor__in=doctors):
            review = Review.objects.filter(doctor__in=doctors).latest('personal', 'empathy')
            result = 'The patient: '+ patient.name + ' can be attended with the doctor: '+review.doctor.name
            return HttpResponse(result)
        return HttpResponse('Does not exist a doctor avilable.')
