from django.contrib import admin
from homes.models import Home, Category


class HomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cost', 'district')
    list_display_links = ('title', 'cost')


admin.site.register(Home, HomeAdmin)
admin.site.register(Category)
