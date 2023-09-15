from rest_framework.viewsets import ModelViewSet

from fabidecor.models import Tema
from fabidecor.serializers import TemaSerializer

class TemaViewSet(ModelViewSet):
    queryset = Tema.objects.all()
    serializer_class = TemaSerializer
