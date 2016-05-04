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

#import other module
from datetime import datetime





#  class based views for attendance_table model--------------------------------------------

class Attendance_tableList(APIView):
    """
    List all attendance_table , or create a new attendance_table

    """
    def get(self, request, format=None):
        attendance_table = Attendance_table.objects.all()
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
            return Attendace_table.objects.get(pk=pk)
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
    #print "datetime",timezone.now()

#----------------------end --------------------------------------------------------------




#  class based views for analysis_table model--------------------------------------------


class Analysis_tableList(APIView):
    """
    List all attendance, or create a new analysis_table.
    """
    def get(self, request,user_id,year,month, format=None):
        analysis_table = Analysis_table.objects.filter(user_id__contains=user_id,attendance_date__year=year,attendance_date__month=month)
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
    def get_object(self, user_id):
        try:
            return Analysis_table.objects.get(user_id=user_id)
        except Analysis_table.DoesNotExist:
            raise Http404

    def get(self, request, user_id,year, format=None):
        analysis_table = self.get_object(user_id)
        serializer = Analysis_tableSerializer(analysis_table)
        return Response(serializer.data)

    def put(self, request, user_id,year, format=None):
        analysis_table = self.get_object(user_id)
        serializer = Analysis_tableSerializer(analysis_table, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id,year, format=None):
        analysis_table = self.get_object(user_id)
        analysis_table.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#------------------------------------end.........................................................
def analysis_table_data():
    return 0

def index(request):
    now=datetime.now()
    user_ids=1030
    login_times=now
    logout_times=now

    print now.day
    while (user_ids!=1050):
        j=1
        k=1
        times=0
        working_hr=0

        query = Attendance_table.objects.filter(user_id__contains = user_ids,created__year=now.year,created__month=now.month,created__day=now.day)
        print "user_id====",user_ids
        for i in query:
            print i
            if(j%2 != 0):
                print "odd===",j
                if(j==1):
                    login_times=i.created
                temp=i.created
                j+=1
            elif(j%2 == 0):
                print "even",j
                timediff = i.created - temp
                times=timediff.total_seconds()
                working_hr=working_hr+times
                j+=1
                print "time in hours====",working_hr/3600

        working_hr=working_hr/3600
        print "times is here ======",working_hr
        j=j-1
        for i in query:
            if(j==k):
                logout_times=i.created
            k+=1

        print "login_times",login_times, "logout_time",logout_times
        analysis_table=Analysis_table(user_id=user_ids,working_hrs=working_hr,login_time=login_times,logout_time=logout_times,state=j)
        analysis_table.save()
        user_ids+=1



    return render(request,'attendance/index.html', {})

# this function for home page
def home(request):
    #analysis_table_object=Analysis_tableList()
    #data=analysis_table_object.get(request,user_id,year,month, format=None)

    return render(request,'attendance/home.html',{})
# Create your views here.
