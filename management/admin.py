from django.contrib import admin

from management.models import *

admin.site.register(Patient)
admin.site.register(Ailment)
admin.site.register(Specialty)
admin.site.register(Doctor)
admin.site.register(Review)
