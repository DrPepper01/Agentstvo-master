from django.shortcuts import render


def contacts_views(request):
    return render(request, 'contacts.html')
