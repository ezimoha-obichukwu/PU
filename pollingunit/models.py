from django.db import models

# Create your models here.
class Pollingunit_Result(models.Model):
    result_id = models.IntegerField()
    polling_unit_uniqueid  = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50, blank=True)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50)

    def __str__(self):
        return self.user_ip_address
    


class LocalGovernment(models.Model):
    name = models.CharField(max_length=100)
    # Add more fields as per your requirements

    def __str__(self):
        return self.name

class PollingUnit(models.Model):
    local_govt = models.ForeignKey(LocalGovernment, on_delete=models.CASCADE)
    summon = models.IntegerField()
    # Add more fields as per your requirements

    def __str__(self):
        return f"PollingUnit {self.id}"



