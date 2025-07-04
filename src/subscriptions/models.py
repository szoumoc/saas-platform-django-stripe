from django.db import models

# Create your models here.
class Subscription(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        permissions = (
            ("basic", "Basic Subscription"), #subscriptions.basic
            ("basic_ai", "Basic AI Subscription"), #subscriptions.basic_ai
            ("pro", "Pro Subscription"), #subscriptions.pro
            ("advanced", "Advanced Subscription"), #subscriptions.advanced
        )