from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from attendance import views

urlpatterns = [
    url(r'^attendance/(?P<user_id>[0-9]+)/(?P<year>[0-9]+)/(?P<month>[0-9]+)/$',views.Analysis_tableList.as_view()),
    url(r'^attendance/detail/(?P<user_id>[0-9]+)/$',views.Analysis_tableDetail.as_view()),

    url(r'^attendance_input/$',views.Attendance_tableList.as_view()),
    url(r'^attendance_input/(?P<pk>[0-9]+)/$',views.Attendance_tableDetail.as_view()),

    #url for JSON data reciever
    url(r'^tracking/$',views.GeodataList.as_view()),
    url(r'^tracking/(?P<pk>[0-9]+)/$',views.GeodataDetail.as_view()),


    #JSON data query response
    url(r'^gpsJSONdata/(?P<user_id>[0-9]+)/(?P<year>[0-9]+)/(?P<month>[0-9]+)/(?P<day>[0-9]+)/$',views.GeodataList2.as_view()),
    url(r'^gpsJSONData/(?P<pk>[0-9]+)/$',views.GeodataDetail.as_view()),

    #url for JSON data reciever for savjiRestaurant
    url(r'^savji_restaurant/$',views.SavjiRestaurantList.as_view()),
    url(r'^savji_restaurant/(?P<pk>[0-9]+)/$',views.SavjiRestaurantDetail.as_view()),


    #url for JSON data reciever for Blog
    url(r'^blogData/$',views.BlogList.as_view()),
    url(r'^blogData/(?P<pk>[0-9]+)/$',views.BlogDetail.as_view()),


    #url for Blog
    url(r'^blog/$',views.blog, name ='blog'),

    #url for tracking
    url(r'^tracker/$',views.tracker, name ='tracker'),

    #url for Si2Tracker.html and Si2Tracker method
    url(r'^trackme/$',views.Si2Tracker, name='Si2Tracker'),

    #url for si2tracker2.html and si2tracker2 method
    url(r'^findyou/$',views.si2tracker2, name='si2tracker2'),

    #url for SavjiRestaurant and savjirestaurant.html
    url(r'^savjirestaurant/$',views.savjirestaurant, name='savjirestaurant'),

    url(r'^index/$',views.index, name = 'index'),

    url(r'^$',views.home, name = 'home'),

    url(r'^dashboard/$',views.chart, name ='chart'),

    url(r'^invoice/$',views.invoice, name ='invoice'),

    url(r'^example/$',views.example, name ='example'),
]

urlpatterns = format_suffix_patterns(urlpatterns)