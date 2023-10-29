class TripStatus:
    DELIVERED = "DELIVERED"
    PICKED = "PICKED"
    AT_VENDOR = "AT_VENDOR"
    ASSIGNED = "ASSIGNED"


TRIP_STATUS_CHOICES = [
    (TripStatus.DELIVERED, TripStatus.DELIVERED),
    (TripStatus.PICKED, TripStatus.PICKED),
    (TripStatus.ASSIGNED, TripStatus.ASSIGNED),
    (TripStatus.AT_VENDOR, TripStatus.AT_VENDOR),
]


class DelayReportResult:
    DURATION_UPDATED = "DURATION_UPDATED"
    ADDED_TO_DELAY_QUEUE = "ADDED_TO_DELAY_QUEUE"


DELAY_REPORT_RESULT_CHOICES = [
    (DelayReportResult.ADDED_TO_DELAY_QUEUE, DelayReportResult.ADDED_TO_DELAY_QUEUE),
    (DelayReportResult.DURATION_UPDATED, DelayReportResult.DURATION_UPDATED),
]