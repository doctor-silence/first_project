from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from orders.models import SalesOrder
from orders.serializers import OrderSerializers


def orders_page(request):
    return render(request, 'index.html', {'orders': SalesOrder.objects.all()})



class OrderView(ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = OrderSerializers


def orders_app(request):
    return render(request, 'main_app.html')