from django.db import models

from django.db import models

class TextContent(models.Model):
    content_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, null=True, blank=True)
    category = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return f"{self.title} ({self.category})"
