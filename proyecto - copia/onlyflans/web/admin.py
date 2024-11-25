from django.contrib import admin
from .models import Flan, ContactForm

# Register your models here.


@admin.register(Flan)
class FlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_private', 'slug')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'contact_form_uuid')
    search_fields = ('customer_name', 'customer_email')
