from django.db import models

from django.conf import settings
from django.core.validators import MinValueValidator


class Expense(models.Model):
    title = models.CharField(max_length=200)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
    )
    category = models.CharField(max_length=100)
    date = models.DateField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='expenses',
    )

    class Meta:
        ordering = ['-date', '-id']

    def __str__(self) -> str:
        return f"{self.title} - {self.amount}"
