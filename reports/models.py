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
class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    index = models.IntegerField()
    date = models.DateField()
    account_number = models.IntegerField()
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    debit = models.DecimalField(max_digits=20, decimal_places=2)
    credit = models.DecimalField(max_digits=20, decimal_places=2)
    source_account_number = models.IntegerField()
    created_at = models.DateTimeField()
    memo = models.TextField()
    source_account = models.TextField()
    payee = models.TextField()
    customer = models.TextField()
    category_account = models.TextField()
    account = models.TextField()
    subcategory = models.TextField()
    project = models.TextField()

    def __str__(self):
        return f"Transaction {self.id}"