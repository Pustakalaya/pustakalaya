from django.contrib import admin
from pustakalaya_apps.collection.models import Collection

from .models import (
    Document,
    DocumentSeries,
    DocumentFileUpload,
    Publisher,
    Note,
)


class DocumentFileUploadInline(admin.StackedInline):
    model = DocumentFileUpload

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    inlines = [
        DocumentFileUploadInline,
    ]


admin.site.register(DocumentFileUpload)
admin.site.register(DocumentSeries)
admin.site.register(Publisher)
admin.site.register(Collection)
admin.site.register(Note)
