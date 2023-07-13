

from django.shortcuts import render

from homes.models import Home


def list_views(request):
    homes = Home.objects.all()
    return render(request, 'index.html', {'homes': homes})


def detail_view(request, pk):
    home = Home.objects.get(id=pk)
    return render(request, 'detail.html', {'home': home})

