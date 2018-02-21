from django.db import models
from django.contrib.auth.models import User
import uuid


class Favourite(models.Model):

    favourite_item_type = models.CharField(max_length=20, null=True)
    favourite_item_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=False)
    user = models.ForeignKey(User)
    addedDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('addedDate',)

    def __str__(self):
        return 'added by {} on {}'.format(self.user, self.addedDate)

