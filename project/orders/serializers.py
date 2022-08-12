from rest_framework.serializers import ModelSerializer

from orders.models import SalesOrder


class OrderSerializers(ModelSerializer):
    class Meta:
        model = SalesOrder
        fields = ['amount', 'description']