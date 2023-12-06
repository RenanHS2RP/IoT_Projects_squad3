from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
from FlowAPIApp.serializers.pumpSerializer import PumpSerializer
from FlowAPIApp.models.pumpModel import PumpFlow
from FlowAPIApp.utils.ThingsBoard import  ThingsBoard

class PumpView(viewsets.ModelViewSet):
    queryset = PumpFlow.objects.all()
    serializer_class = PumpSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            thingsBoard = ThingsBoard('token')
            thingsBoard.post_telemetry(serializer.data)

            return Response({"success": "Dados salvos com sucesso", "data": serializer.data}, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": "Erro de validação", "detail": e.args}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"error": 'Erro', "detail": e.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
