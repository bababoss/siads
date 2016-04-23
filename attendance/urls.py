from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from attendance import views

urlpatterns = [
    url(r'^attendance/(?P<user_id>[0-9]+)/(?P<year>[0-9]+)/(?P<month>[0-9]+)/$',views.Analysis_tableList.as_view()),
    url(r'^attendance/detail/(?P<user_id>[0-9]+)/$',views.Analysis_tableDetail.as_view()),
    url(r'^attendance_input/(?P<user_id>[0-9]+)/$',views.Attendance_tableList.as_view()),
    url(r'^attendance_input/(?P<pk>[0-9]+)/$',views.Attendance_tableDetail.as_view()),
    url(r'^index/$',views.index, name = 'index'),
]

urlpatterns = format_suffix_patterns(urlpatterns)