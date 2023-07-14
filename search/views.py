from django.shortcuts import render

from homes.models import Home


def search_views(request):
    query = request.GET.get('q')
    big = request.GET.get('max')
    small = request.GET.get('min')

    if query:
        homes = Home.objects.filter(info__iregex=query)
    else:
        homes = Home.objects.all()

    if big:
        homes = homes.filter(cost__lte=big)
    if small:
        homes = homes.filter(cost__gte=small)

    return render(request, 'search.html', {'homes': homes})
