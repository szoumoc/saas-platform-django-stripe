from django.db import models
from django.contrib.auth.models import Group, Permission


SUBSCRIPTION_PERMISSIONS = [
    ("advanced", "Advanced Perm"), # subscriptions.advanced
    ("pro", "Pro Perm"),  # subscriptions.pro
    ("basic", "Basic Perm"),  # subscriptions.basic,
    ("basic_ai", "Basic AI Perm")
]

# Create your models here.
class Subscription(models.Model):
    name = models.CharField(max_length=100)
    groups = models.ManyToManyField(Group)
    permissions =  models.ManyToManyField(Permission, limit_choices_to={
        "content_type__app_label": "subscriptions", "codename__in": [x[0]for x in SUBSCRIPTION_PERMISSIONS]
    })

    class Meta:
        permissions = SUBSCRIPTION_PERMISSIONS