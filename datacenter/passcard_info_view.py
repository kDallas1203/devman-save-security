from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone

def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []

    for visit in visits:
        duration = visit.get_duration()
        this_passcard_visits.append({
            "entered_at":
            timezone.localtime(visit.entered_at),
            "duration":
            visit.format_duration(duration),
            "is_strange":
            visit.is_visit_long()
        })

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
