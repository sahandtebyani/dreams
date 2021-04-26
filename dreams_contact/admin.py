from django.contrib import admin
from dreams_contact.models import ContactUs


class ConatacAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'subject', 'is_read']
    list_filter = ['is_read']

admin.site.register(ContactUs, ConatacAdmin)
