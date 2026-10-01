from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nombre', 'categoria']

    @action(detail=False, methods=['get'])
    def solo_stock(self, request):
        productos_con_stock = self.queryset.filter(stock=True)
        serializer = self.get_serializer(productos_con_stock, many=True)
        return Response(serializer.data)