from django.contrib import admin
from .models import Pollingunit_Result, LocalGovernment, PollingUnit #Party, PollingUnitResult2, PollingUnit2

# Register your models here.
admin.site.register([Pollingunit_Result, LocalGovernment, PollingUnit]) 