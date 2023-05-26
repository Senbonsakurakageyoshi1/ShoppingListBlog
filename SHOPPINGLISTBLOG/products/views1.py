from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers1 import ProductSerializer
from .models import Produits


class ProductViewSet(ReadOnlyModelViewSet):

    serializer_class = ProductSerializer
    queryset = Produits.objects.all()


    
    def get_list(self, request):
        pass
      
   
    def get_product(self, request, pk=None):
        pass


    
    def delete_product(self, request, pk=None):
        pass