from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Fund
from .serializers import FundSerializer

@api_view(['GET'])
def fund_list(request):
    funds = Fund.objects.all()  # Get all fund entries
    serializer = FundSerializer(funds, many=True)  # Convert to JSON
    return Response(serializer.data)

