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
from  django.utils.html import format_html


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )
    list_display = ['sponsor_name_', 'edit_link', ]

    def sponsor_name_(self, obj):
        return obj.name

    def edit_link(self, obj):
        return format_html("<a href='{url}'>Edit</a>", url=obj.get_admin_url())



@admin.register(LicenseType)
class LicenseTypeAdmin(admin.ModelAdmin):
    search_fields = (
        'license',
    )

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

    list_display = ['author', 'edit_link']
    search_fields = (
        'name',
    )

    def author(self,obj):
        return format_html('<a href="%s">%s</a>' % (obj.get_absolute_url(), obj.getName()))

    def edit_link(self, obj):
        return format_html("<a href='{url}'>Edit</a>", url=obj.get_admin_url())


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    search_fields = (
        'publisher_name',
    )
    list_display = ['Publisher_Name', 'edit_link',]

    def Publisher_Name(self,obj):
        return obj.publisher_name


    def edit_link(self, obj):
        return format_html("<a href='{url}'>Edit</a>", url=obj.get_admin_url())

@admin.register(EducationLevel)
class EducationLevelAdmin(admin.ModelAdmin):
    pass

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    search_fields = (
        'language',
    )
