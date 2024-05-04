from django.contrib import admin
from .models import PetAdd


#new code:


@admin.register(PetAdd)
class PetAddAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'price', 'available')
    list_filter = ('species', 'available')
    search_fields = ('name', 'species')
    actions = ['mark_as_sold', 'mark_as_available']

    def mark_as_sold(self, request, queryset):
        queryset.update(available=False)

    def mark_as_available(self, request, queryset):
        queryset.update(available=True)

admin.site.site_header = 'Pet Store Administration'
admin.site.site_title = 'Pet Store Admin'
admin.site.index_title = 'Welcome to the Pet Store Admin Panel'
