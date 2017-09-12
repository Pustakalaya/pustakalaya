from django.contrib import admin
from .models import (
    Keyword,
    Category,
    Biography
)

admin.site.register(Keyword)
admin.site.register(Category)
admin.site.register(Biography)
