from django.db import models

RATED = (
    (0, "Default"),
    (1, "Very Bad"),
    (2, "Bad"),
    (3, "Normal"),
    (4, "Good"),
    (5, "Best Ever"),
)

RESOLVED_TYPE = (
    (0, "Default"),
    (1, "return order"),
    (2, "save order and 20% discout"),
    (3, "change thing/s"),
)

STATUS_COMPLAINT = (
    (0, "Default"),
    (1, "New"),
    (2, "In progress"),
    (3, "Resolved"),
)


# Create your models here.
class Opinion(models.Model):
    """
    Opinion model
    """
    nickname = models.CharField(max_length=25, null=False)
    rated = models.IntegerField(choices=RATED, null=False)
    textOpinion = models.TextField(null=False)
    dateOpinion = models.DateField(null=False)


class Complaint(models.Model):
    """
    Complaint model
    """
    first_name = models.CharField(max_length=25, null=False)
    last_name = models.CharField(max_length=25, null=False)
    order_numer = models.CharField(max_length=8, null=False)
    textComplaint = models.TextField(null=False)
    dateComplaint = models.DateField(null=False)
    resolved_type = models.CharField(choices=RESOLVED_TYPE, null=False)
    status = models.CharField(choices=STATUS_COMPLAINT, null=False)
