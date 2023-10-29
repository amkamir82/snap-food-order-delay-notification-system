from datetime import datetime

from django.db import models

from core.models import BaseModel
from shop.statics import TRIP_STATUS_CHOICES, TripStatus, DELAY_REPORT_RESULT_CHOICES


class Vendor(BaseModel):
    name = models.CharField(max_length=16)


class Order(BaseModel):
    vendor = models.ForeignKey(to=Vendor, on_delete=models.CASCADE, related_name="orders")
    delivery_duration = models.DurationField()
    delivery_time = models.DateTimeField()

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.pk:
            start = datetime.now()
        else:
            start = self.created
        self.delivery_time = self.delivery_duration + start
        return super(Order, self).save(force_insert, force_update, using, update_fields)


class Agent(BaseModel):
    name = models.CharField(max_length=16)
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, related_name="agent", null=True)


class Trip(BaseModel):
    order = models.OneToOneField(to=Order, on_delete=models.DO_NOTHING, related_name="trip")
    status = models.CharField(max_length=16, choices=TRIP_STATUS_CHOICES, default=TripStatus.AT_VENDOR)


class DelayReport(BaseModel):
    name = models.CharField(max_length=16)
    result = models.CharField(max_length=32, choices=DELAY_REPORT_RESULT_CHOICES)
    trip = models.ForeignKey(to=Trip, on_delete=models.CASCADE, related_name="delay_reports", null=True)
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, related_name='delay_reports')


class DelayQueueItem(BaseModel):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, related_name="queue_item", null=True)

