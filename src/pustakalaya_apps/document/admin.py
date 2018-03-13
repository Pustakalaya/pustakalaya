from  django.utils.html import format_html
from django.contrib import admin

from .models import (
    Document,
    UnpublishedDocument,
    DocumentSeries,
    DocumentFileUpload,
    DocumentLinkInfo,
    DocumentIdentifier
)


class DocumentFileUploadInline(admin.TabularInline):
    model = DocumentFileUpload
    extra = 1
    fields = ["upload"]


class DocumentLinkInfoAdminInline(admin.TabularInline):
    model = DocumentLinkInfo
    extra = 1


class DocumentIdentifierAdmin(admin.StackedInline):
    model = DocumentIdentifier
    extra = 1
    max_num = 1

@admin.register(DocumentSeries)
class DocumentSeriesAdmin(admin.ModelAdmin):
    pass


@admin.register(UnpublishedDocument)
class UnpublishedDocumentAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return  self.model.objects.filter(published="no")

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    inlines = [
        DocumentIdentifierAdmin,
        DocumentLinkInfoAdminInline,
        DocumentFileUploadInline,
    ]

    search_fields = (
        'title',
    )

    fields = (
        "title",
        "abstract",
        "collections",
        "education_levels",
        "languages",
        "featured",
        "published",
        "document_file_type",
        "document_interactivity",
        "document_authors",
        "document_editors",
        "document_illustrators",
        "place_of_publication",
        "publisher",
        "publication_year_on_text",
        "year_of_available_on_text",
        "keywords",
        "document_series",
        "volume",
        "edition",
        "document_total_page",
        "document_type",
        "additional_note",
        "description",
        "license",
        "custom_license",
        "sponsors",
        "thumbnail",
    )

    list_display = ['title_link', 'published_','featured_', 'edit_link', 'updated_date_', 'submitted_by_']

    ordering = ('-updated_date',)


    list_filter = ['published', 'title','featured']

    list_per_page = 10

    def save_model(self, request, obj, form, change):
        """Override the submitted_by field to admin user
        save_model is only called when the user is logged as an admin user.
        """
        if obj.submitted_by is None:
            obj.submitted_by = request.user
        super().save_model(request, obj, form, change)

    def edit_link(self, obj):
        return format_html("<a href='{url}'>Edit</a>", url=obj.get_admin_url())

    def title_link(self,obj):
        return format_html('<a href="%s">%s</a>' %(obj.get_absolute_url(), obj.document_title()))


    def published_(self,obj):
        return format_html('%s' % (obj.published_yes_no()))

    def featured_(self,obj):
        return format_html('%s' % (obj.featured_yes_no()))

    def updated_date_(self,obj):
        return format_html('%s' % (obj.updated_date_string()))

    def submitted_by_(self,obj):
        return format_html('%s' % (obj.submited_by()))



