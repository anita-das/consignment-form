from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class ConsignmentItem(models.Model):
    bulkInd = models.BooleanField()
    brand = models.CharField(max_length=200)
    size = models.CharField(max_length=3)
    initialPrice = models.DecimalField(max_digits=5, decimal_places=2)
    lowestPrice = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    acceptedInd = models.BooleanField()

    # def publish(self):
    #     self.created_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.description
