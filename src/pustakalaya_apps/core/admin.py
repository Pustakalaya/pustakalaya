from django.contrib import admin
from .models import (
    Keyword,
    Category,
    Biography,
    Sponsor,
)


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


@admin.register(Keyword)
class KeyWordAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class PublisherAdmin(admin.ModelAdmin):
    pass

# admin.site.register(DocumentFileUpload)
