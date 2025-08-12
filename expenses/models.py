from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.utils import timezone

class Group(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Label(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='labels')
    monthly_expected_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Optional monthly expected amount"
    )
    def __str__(self):
        return f"{self.name} ({self.group.name})"

class Expense(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='expenses')
    label = models.ForeignKey(Label, on_delete=models.CASCADE, related_name='expenses')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)  # default to today but editable

    def __str__(self):
        return f"{self.amount} - {self.label.name} - {self.user.username}"

class Income(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='incomes')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)  # Auto today, but editable

    def __str__(self):
        return f"Income: {self.amount} on {self.date}"