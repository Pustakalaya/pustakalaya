from django.contrib import admin
from .models import Community
from pustakalaya_apps.collection.models import Collection


class CollectionInline(admin.StackedInline):
    model = Collection


@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    inlines = [
        CollectionInline,
    ]
