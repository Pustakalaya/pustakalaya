from django.db import models
from django.utils.translation import ugettext as _


class ItemCategory(models.Model):
    category_name = models.CharField(
        _("Item Category"),
        max_length=255,
    )

    category_description = models.TextField(
        verbose_name=_("Item category description")
    )

    def __str__(self):
        return self.category_name




