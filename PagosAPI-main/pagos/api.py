from .models import Pagos
from rest_framework import viewsets
from .serializers import PagoSerializer
from rest_framework.permissions import IsAuthenticated
from .pagination import StandardResultsSetPagination
from rest_framework import viewsets, filters 

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pagos.objects.get_queryset().order_by('id')
    serializer_class = PagoSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    #permission_classes = [IsAuthenticated]

    search_fields = ['fecha_pago']
    throttle_scope = 'pagos'