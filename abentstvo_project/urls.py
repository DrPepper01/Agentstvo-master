from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from contacts.views import contacts_views
from homes.views import list_views, detail_view

from abentstvo_project import settings
from search.views import search_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_views, name='main_page'),
    path('home/<int:pk>', detail_view, name='detail_page'),
    path('search', search_views, name='search_page'),
    path('contacts', contacts_views, name='contacts_page'),

]


if settings.DEBUG is True:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)