from django.db import models

from cat.models import Cat


class Mission(models.Model):
    name = models.CharField(max_length=255)
    cat = models.ForeignKey(
        Cat, on_delete=models.CASCADE, null=True, blank=True
    )  # Allow null for unassigned missions
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Target(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    notes = models.TextField()
    is_completed = models.BooleanField(default=False)
    mission = models.ForeignKey(Mission, related_name='targets', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
