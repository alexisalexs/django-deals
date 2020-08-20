from .models import Item
from .serializers import ItemSerializer
from rest_framework import generics

class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer