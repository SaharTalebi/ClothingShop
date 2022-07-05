from django.contrib import admin

from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display =('id', 'name', 'email', 'subject')
    list_display_links = ('name', 'email',)

admin.site.register(Contact, ContactAdmin)
