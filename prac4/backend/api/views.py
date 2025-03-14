from rest_framework.permissions import IsAuthenticated 
from rest_framework import viewsets
from .permissions import IsAdmin 
from api.models import Item
from api.serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet): 

    queryset = Item.objects.all() 

    serializer_class = ItemSerializer 

 

    def get_permissions(self): 

        if self.request.method in ['POST', 'PUT', 'DELETE']: 

            return [IsAuthenticated(), IsAdmin()] 

        return [IsAuthenticated()] 

 