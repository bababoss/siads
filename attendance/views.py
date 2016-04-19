from django.shortcuts import render
#---------------------Its for function based views-----------------------
#from django.http import HttpResponse
#from django.views.decorators.csrf import csrf_exampt
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser

#------------ ---------------------- ---------------- ---------

#---------Usins class based views--------------------
from attendance.models import Analysis_table
from attendance.models import Attendance_table
from attendance.serializers import Analysis_tableSerializer
from attendance.serializers import Attendance_tableSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#  class based views for attendance_table model--------------------------------------------

class Attendance_tableList(APIView):
    """
    List all attendance_table , or create a new attendance_table
    
    """
    def get(self, request, format=None):
        attendance_table = attendance_table.object.all()
        serializer  = Attendance_tableSerializer(attendance_table,many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = Attendance_tableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Attendance_tableDetail(APIView):
    """
    Retrive , update, or delete a attendance_table instance.
    
    """
    def get_object(self,pk):
        try:
            return Attendace_table.object.get(pk=pk)
        except Attendance_table.DoseNotExit:
            raise Http4014
    def get(self, request, pk, format=None):
        attendance_table = self.get_object(pk)
        serializer=Attendance_tableSerializer(attendance_table)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        attendance_table=self.get_object(pk)
        serializer=Attendance_tableSerializer(attendance_table,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status.status.HTTP_400_BAD_REQUESt)
    def delete(self, request, pk, format=None):
        attendance_table=self.get_object(pk)
        attendance_table.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#----------------------end --------------------------------------------------------------    



    
#  class based views for analysis_table model--------------------------------------------


class Analysis_tableList(APIView):
    """
    List all attendance, or create a new analysis_table.
    """
    def get(self, request, format=None):
        analysis_table = Analysis_table.objects.all()
        serializer = Analysis_tableSerializer(analysis_table, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Analysis_tableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Analysis_tableDetail(APIView):
    """
    Retrieve, update or delete a analysis_table instance.
    """
    def get_object(self, pk):
        try:
            return Analysis_table.objects.get(pk=pk)
        except Analysis_table.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        analysis_table = self.get_object(pk)
        serializer = Analysis_tableSerializer(analysis_table)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        analysis_table = self.get_object(pk)
        serializer = Analysis_tableSerializer(analysis_table, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        analysis_table = self.get_object(pk)
        analysis_table.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#------------------------------------end.........................................................
# Create your views here.
