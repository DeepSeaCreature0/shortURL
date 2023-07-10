from django.contrib import admin
from .models import link

# Register your models here.
@admin.register(link)
class AdminLink(admin.ModelAdmin):
    list_display=('actual_url','short_url','hit_count','expired')