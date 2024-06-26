from django.db import models
from django.conf import settings

class Favorite(models.Model):
  id = models.AutoField(primary_key=True)
  user_id = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='favorites')
  track_id = models.ForeignKey('Track', related_name='track', on_delete=models.CASCADE)
  class Meta:
    unique_together = ['user_id', 'track_id']