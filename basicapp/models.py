from django.db import models


# Create your models here.
class JournalModel(models.Model):
    title = models.CharField(max_length=100, blank=True, null=False, default=None)
    description = models.CharField(max_length=100, blank=True, null=True, default=None)
    author = models.CharField(max_length=100, blank=True, null=True, default=None)

    class Meta:
        db_table = 'Journalinfo'
