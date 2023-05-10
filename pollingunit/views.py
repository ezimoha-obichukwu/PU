from django.shortcuts import render
from django.db.models import Sum
from .models import Pollingunit_Result, LocalGovernment, PollingUnit
from django.http import HttpResponse

# Create your views here.
def pu_result(request):
    all_unit = Pollingunit_Result.objects.all()
    context = {
        "all_unit": all_unit
    }
    return render(request, "pu_result.html", context)


def summon_result(request):
    if request.method == 'POST':
        local_govt_id = request.POST.get('local_govt')
        try:
            local_govt = LocalGovernment.objects.get(id=local_govt_id)
            polling_units = PollingUnit.objects.filter(local_govt=local_govt)
            total_summon = sum([unit.summon for unit in polling_units])
            context = {
                'local_govts': local_govt,
                'polling_units': polling_units,
                'total_summon': total_summon,
            }
            return render(request, 'summon_result.html', context)
        except LocalGovernment.DoesNotExist:
            return HttpResponse('Local government not found')
    else:
        local_govts = LocalGovernment.objects.all()
        context = {
            'local_govts': local_govts,
        }
        return render(request, 'select_local_govt.html', context)
    

