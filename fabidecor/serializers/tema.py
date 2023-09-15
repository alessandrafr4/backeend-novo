from rest_framework.serializers import ModelSerializer

from fabidecor.models import Tema

class TemaSerializer(ModelSerializer):
    class Meta:
        model = Tema
        fields = "__all__"
        depth = 1
 