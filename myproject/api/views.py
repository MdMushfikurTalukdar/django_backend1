from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import RoomBooking
from .serializers import RoomBookingSerializer

class RoomBookingView(APIView):
    def get(self, request):
        query = request.GET.get('query', '')
        bookings = RoomBooking.objects.filter(room_name__icontains=query)
        serializer = RoomBookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoomBookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
