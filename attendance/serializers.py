
from rest_framework import serializers
from attendance.models import Analysis_table, Attendance_table, Geodata,SavjiRestaurant,Blog, LANGUAGE_CHOICES, LEXERS, STYLE_CHOICES

#SnippetSerializer class is replicating a lot of information that's also contained in the Attendance_table model
class Attendance_tableSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance_table
        fields = ('id','user_id','created')

#SnippetSerializer class is replicating a lot of information that's also contained in the Analysis_table model

class Analysis_tableSerializer(serializers.ModelSerializer):
    class Meta:
        model=Analysis_table
        fields = ('id','user_id','attendance_date','working_hrs','login_time','logout_time','state')

#serilaizer class for Geodata table
class GeodataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Geodata
        fields = ('id','user_id','device_id','latitude','longitude','speed','time_stamp')

#serilaizer class for  table
class SavjiRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model=SavjiRestaurant
        fields = ('id','username','contact','item1','item2','cost','time_stamp')

#serilaizer class for  table Blog
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields = ('id','title','body','publish_date','topic','topic_content','code','gPlus')