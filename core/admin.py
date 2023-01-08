from django.contrib import admin
from .models import Patient 

# Register your models here.


class PatientAdmin(admin.ModelAdmin):
    list_display=('full_name', 'mobile_no', 'detail', 'precaution', 'visit_date', 'next_visit_date')
admin.site.register(Patient, PatientAdmin)


