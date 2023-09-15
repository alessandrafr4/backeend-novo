from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer
from rest_framework.permissions import IsAuthenticated

from fabidecor.models import Categoria, Produto, Tema
from fabidecor.serializers import CategoriaSerializer, ProdutoSerializer, ProdutoSerializer, TemaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]

class TemaViewSet(ModelViewSet):
    queryset = Tema.objects.all()
    serializer_class = TemaSerializer

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


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
    

    

