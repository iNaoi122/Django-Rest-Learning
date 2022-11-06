from .serializers import Serializers, SerializersNotModel
# Create your views here.
from .models import Character
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView


class Api(APIView):
    def get(self, request):
        chrs = Character.objects.all()
        return Response({"post":Serializers(chrs, many=True).data})

    def post(self, request):
        serializer = Serializers(data=request.data)
        serializer.is_valid(raise_exception=True)

        new = Character.objects.create(
            name = request.data["name"],
            age = request.data["age"],
            content = request.data["content"],
            )
        return Response({"post": Serializers(new).data})

    def put(self, request, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Not found"})
        try:
            instance = Character.objects.get(pk=pk)
        except:
            return  Response({"error":"Object doesn't exist"})

        serializer = Serializers(data = request.data, instance = instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post":serializer.data})

    def delete(self, request, **kwargs):
        pk = kwargs.get("pk")
        if not pk:
            return Response({"error":"Not found"})
        try:
            Character.objects.get(pk=pk).delete()
        except:
            return Response({"error":"Object doesn't exist "})
        return Response({"delete":"Yes"})


"""class Api (generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = Serializers"""