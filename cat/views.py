from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import Cat
from .serializers import CatSerializer
from .utils import validate_breed


class CatList(APIView):
    def get(self, request):
        cats = Cat.objects.all()
        serializer = CatSerializer(cats, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid() and validate_breed(request.data["breed"]):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CatDetails(APIView):
    def get(self, request, id):
        cat = get_object_or_404(Cat, pk=id)
        serializer = CatSerializer(cat)
        return Response(serializer.data)

    def patch(self, request, id):
        cat = get_object_or_404(Cat, pk=id)
        serializer = CatSerializer(cat, data=request.data, partial=True)

        if "breed" in request.data:
            if not validate_breed(request.data["breed"]):
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        cat = Cat.objects.get(pk=id)
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
