#from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Enroll
from rest_framework import status
from .serializer import EnrolSerializer
# Create your views here.

@api_view(['POST'])

def postenroll(request):


    student = EnrolSerializer(data = request.data)
    if student.is_valid():
        student.save()
        return Response(student.data, status = status.HTTP_201_CREATED)
    else:
        return Response(student.data, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])

def getEnroll(request):

    data=Enroll.objects.all()
    student = EnrolSerializer(data,many=True)
    
    return Response(student.data, status = status.HTTP_201_CREATED)


