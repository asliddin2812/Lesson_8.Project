from drf_yasg import openapi
from drf_yasg.openapi import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import OmonimTafsiloti, Omonimlar
from .serializers import OmonimlarTafsilotiSerializer,OmonimlarSerializer


@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter(
            'name',
            openapi.IN_QUERY,
            description="Qidirilayotgan omonim nomi (masalan: olma)",
            type=openapi.TYPE_STRING
        )
    ],
    responses={200: OmonimlarSerializer(many=True)}
)
@api_view(['GET'])
def omonimlar_search(request):
    name = request.GET.get('name')
    if not name:
        return Response({"error": "Iltimos, 'name' parametrini kiriting"}, status=400)

    queryset = Omonimlar.objects.filter(name=name)
    serializer = OmonimlarSerializer(queryset, many=True)
    return Response(serializer.data)
@swagger_auto_schema(method = 'post', request_body=OmonimlarTafsilotiSerializer)
@api_view(['POST'])
def omonim_view(request):
    serializer = OmonimlarTafsilotiSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='post', request_body=OmonimlarSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def omonim_create(request):
    serializer = OmonimlarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)