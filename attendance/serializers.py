
from rest_framework import serializers
from attendance.models import Analysis_table, Attendance_table, LANGUAGE_CHOICES, LEXERS, STYLE_CHOICES

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
        