from django.contrib import admin
from .models import (
    Keyword,
    Category,
    Biography,
    Sponsor,
    Publisher
)


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
   pass

@admin.register(Keyword)
class KeyWordAdmin(admin.ModelAdmin):
    pass


@admin.register(Biography)
class BiographyAdmin(admin.ModelAdmin):
    pass


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass


