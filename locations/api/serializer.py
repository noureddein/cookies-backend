from rest_framework import serializers
from locations.models import DailyCookies


class CookiesLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyCookies
        fields = (
                    'id',
                    'location',
                    'minCostumer',
                    'maxCostumer',
                    'avgCookie',
                )