from django.db import models

# Create your models here.

class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Zone(AbstractBaseModel):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    coordinates = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Visitors(AbstractBaseModel):
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name='visitors')
    full_name = models.CharField(max_length=150)
    info = models.TextField(blank=True, null=True)
    is_allowed = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name