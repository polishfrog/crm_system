from django.db import models

RATED = (
    (0, "Default"),
    (1, "Very Bad"),
    (2, "Bad"),
    (3, "Normal"),
    (4, "Good"),
    (5, "Best Ever"),
)


# Create your models here.
class Opinion(models.Model):
    """
    Opinion model
    """
    nickname = models.CharField(max_length=25, null=False)
    rated = models.CharField(max_length=50, choices=RATED, null=False)
    textOpinion = models.TextField(null=False)
    dateOpinion = models.DateField(null=False)

