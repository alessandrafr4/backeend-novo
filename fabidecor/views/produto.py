from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer

from fabidecor.models import Produto 
from fabidecor.serializers import ProdutoSerializer

class ProdutoDetailSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
        depth = 1

class ProdutoListSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = ["id", "Tema", "preco"]

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ProdutoDetailSerializer
        return ProdutoSerializer
    

    
