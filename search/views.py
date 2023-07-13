from django.shortcuts import render

from homes.models import Home


def search_views(request):
    homes = Home.objects.all()

    return render(request, 'search.html', {'homes': homes})
