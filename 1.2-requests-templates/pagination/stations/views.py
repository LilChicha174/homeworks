import csv
import pagination.settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    stations = []
    csv_ph = pagination.settings.BUS_STATION_CSV
    print(csv_ph)
    with open(csv_ph, newline='', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for i in reader:
            stations += [i]
    paginator = Paginator(stations, 3)
    page_number = int(request.GET.get("page", 1))
    stations_list = paginator.get_page(page_number)

    context = {
        'bus_stations': stations_list,
        'page': stations_list,
    }
    return render(request, 'stations/index.html', context)
