from django.contrib import admin
from pustakalaya_apps.collection.models import Collection

from .models import (
    Document,
    DocumentSeries,
    DocumentFileUpload,
    Publisher,
)


class DocumentFileUploadInline(admin.TabularInline):
    model = DocumentFileUpload
    extra = 1



@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    inlines = [
        DocumentFileUploadInline,
    ]

@admin.register(DocumentSeries)
class DocumentSeriesAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

#admin.site.register(DocumentFileUpload)


