from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from attendance import views

urlpatterns = [
    url(r'^attendance/$',views.Analysis_tableList.as_view()),
    url(r'^attendance/(?P<pk>[0-9]+)/$',views.Analysis_tableDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)