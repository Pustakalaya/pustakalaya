from django.contrib import admin

from .models import (
    Document,
    DocumentAuthor,
    DocumentEditor,
    DocumentIllustrator,
    DocumentSeries,
    DocumentFileUpload,
    Note
)

from pustakalaya_apps.collection.models import Collection


admin.site.register(Document)
admin.site.register(DocumentAuthor)
admin.site.register(DocumentEditor)
admin.site.register(DocumentFileUpload)
admin.site.register(DocumentSeries)
admin.site.register(DocumentIllustrator)
admin.site.register(Collection)
admin.site.register(Note)
