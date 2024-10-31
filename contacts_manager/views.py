import pandas as pd

from rest_framework import status, viewsets
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import PhoneNumber
from .serializers import PhoneNumberSerializer


class UploadExcelView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        file = request.FILES['file']

        df = pd.read_excel(file, usecols=['mobile'])

        phone_numbers = [
            PhoneNumber(phone_number=row['mobile']) for _, row in df.iterrows()
        ]

        BULK_LIMIT = 1000
        for i in range(0, len(phone_numbers), BULK_LIMIT):
            PhoneNumber.objects.bulk_create(phone_numbers[i:i + BULK_LIMIT])

        return Response({'message': 'Excel file uploaded successfully'}, status=status.HTTP_201_CREATED)


class PhoneNumberViewSet(viewsets.ModelViewSet):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer
