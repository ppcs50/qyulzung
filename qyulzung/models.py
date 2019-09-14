from django.contrib.auth.models import User
from django.db import models
from datetime import date

# Create your models here.
class QZ(models.Model):
    topic = models.CharField(max_length=128)
    user = models.ForeignKey(User, null=True, blank=True, on_delete='CASCADE')
    date = models.DateField(("Date"), auto_now_add=True)
    time = models.TimeField(("Time"), auto_now_add=True, blank=True)
    alt1 = models.CharField(max_length=128, null=True, blank=True)
    alt1sco = models.IntegerField(null=True, blank=True)
    alt2 = models.CharField(max_length=128, null=True, blank=True)
    alt2sco = models.IntegerField(null=True, blank=True)
    alt3 = models.CharField(max_length=128, null=True, blank=True)
    alt3sco = models.IntegerField(null=True, blank=True)
    cr1 = models.CharField(max_length=128, null=True, blank=True)
    cr1sco = models.IntegerField(null=True, blank=True)
    cr2 = models.CharField(max_length=128, null=True, blank=True)
    cr2sco = models.IntegerField(null=True, blank=True)
    cr3 = models.CharField(max_length=128, null=True, blank=True)
    cr3sco = models.IntegerField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    ongoing = models.BooleanField()
    post_yn = models.BooleanField()

    def __str__(self):
        return f"{self.topic}"

class Topic(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
