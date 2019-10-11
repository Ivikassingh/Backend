
from rest_framework.views import  APIView
from rest_framework.response import  Response
from rest_framework import status
import datetime

from . import models
from . import serializer


class Orders(APIView):
    def get(self, request, format=None):
        data_results = models.Orders.objects.all()
        serialize = serializer.OrdersFoodSerializer(data_results, many=True)
        return Response(serialize.data)

    def post(self, request, format=None):
        date=request.data["date"]
        ls=date.split("-")
        print(ls)
        newdate=ls[2]+"-"+ls[1]+"-"+ls[0]
        newdata={}
        newdata["date"]=date
        print(newdata)
        serialize = serializer.OrdersFoodSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)



# class TravelDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.TravelCustomize.objects.all()
#     serializer_class = serializer.TraveCustomizeSerializer



class OrdersDetail(APIView):

    def get_object(self, pk):
        try:
            return models.Orders.objects.get(pk=pk)
        except models.Orders.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        data_result = self.get_object(pk)
        serialize = serializer.OrdersFoodSerializer(data_result)
        return Response(serialize.data)

    def put(self, request, pk, format=None):
        data_result = self.get_object(pk)
        serialize = serializer.OrdersFoodSerializer(data_result, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        data_result = self.get_object(pk)
        data_result.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

###################################################################################### 
class Locations(APIView):
    def get(self, request, format=None):
        data_results = models.Locations.objects.all()
        serialize = serializer.LocationSerializer(data_results, many=True)
        return Response(serialize.data)

class Restaurant(APIView):
    def get(self, request, format=None):
        data_results = models.Restaurant.objects.all()
        serialize = serializer.RestaurantSerializer(data_results, many=True)
        return Response(serialize.data)

class FoodList(APIView):
    def get(self, request, format=None):
        data_results = models.FoodList.objects.all()
        serialize = serializer.FoodListSerializer(data_results, many=True)
        return Response(serialize.data)