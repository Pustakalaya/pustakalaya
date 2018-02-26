from django.contrib import admin
from .models import Review
# Register your models here.


class ReviewAdmin(admin.ModelAdmin):

    list_display = ('content_id', 'user', 'post', 'created', 'published')

    search_fields = ('user','post','published')
    list_filter = ('published',)
    # def get_queryset(self, request):
    #     return self.model.objects.filter(published="False")


admin.site.register(Review,ReviewAdmin)
