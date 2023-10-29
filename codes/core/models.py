from django.db import models


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class BaseModel(models.Model):
    objects = models.Manager()
    active_objects = ActiveManager()

    created = models.DateTimeField(
        auto_now_add=True,
    )

    modified = models.DateTimeField(
        auto_now=True,
    )

    is_deleted = models.BooleanField(
        default=False,
    )

    is_archived = models.BooleanField(
        default=False,
    )

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.is_archived = True
        self.save()
