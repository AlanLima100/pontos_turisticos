from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuriscoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = PontoTuristico.objects.all()
    # cara como você quer mostrar esse dado, quais campos voc~e quer que eu inclua no JSON?
    serializer_class = PontoTuristicoSerializer  
