# yourapp/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import RelaxedFit, RegularFit
from .serializers import RelaxedFitSerializer, RegularFitSerializer

class FitTypeAPIView(APIView):
    def get(self, request, *args, **kwargs):
        type_of_fit = request.query_params.get('type_of_fit')
    
        if type_of_fit == 'relaxed':
            data = RelaxedFit.objects.all()
            serializer = RelaxedFitSerializer(data, many=True)
        elif type_of_fit == 'regular':
            data = RegularFit.objects.all()
            serializer = RegularFitSerializer(data, many=True)
        else:
            return Response({'error': 'Invalid type_of_fit parameter'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'data': serializer.data})
