from django.contrib import admin
from .models import (
    Keyword,
    Biography,
    Sponsor,
    Publisher,
    EducationLevel,
    Language,
    LicenseType

)


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
   pass

@admin.register(LicenseType)
class LicenseTypeAdmin(admin.ModelAdmin):
   pass

@admin.register(Keyword)
class KeyWordAdmin(admin.ModelAdmin):
    pass


@admin.register(Biography)
class BiographyAdmin(admin.ModelAdmin):
    exclude = [
        'first_name',
        'middle_name',
        'last_name',
    ]


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass

@admin.register(EducationLevel)
class EducationLevelAdmin(admin.ModelAdmin):
    pass

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass
