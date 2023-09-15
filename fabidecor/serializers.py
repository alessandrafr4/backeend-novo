from rest_framework.serializers import ModelSerializer

from fabidecor.models import Categoria, Produto, Tema

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"

class TemaSerializer(ModelSerializer):
    class Meta:
        model = Tema
        fields = "__all__"
        depth = 1
 