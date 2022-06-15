from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.postgres.fields import ArrayField
"""

const x = [
  {
    cookiesPerHour: [28, 28, 103, 45, 19, 27, 87, 54, 74, 81, 17, 23, 8, 77],
    location: "amman",
    totalCookiesDaily: 671,
  },
];

"""

class DailyCookies(models.Model):
    location = models.CharField(max_length=64)
    minCostumer = models.IntegerField()
    maxCostumer = models.IntegerField()
    avgCookie = models.FloatField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.location
