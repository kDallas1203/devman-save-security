from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = []

    for visit in visits:
      duration = visit.get_duration()

      non_closed_visits.append({
        "who_entered": visit.passcard.owner_name,
        "entered_at": timezone.localtime(visit.entered_at),
        "duration": visit.format_duration(duration)
      })

    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
