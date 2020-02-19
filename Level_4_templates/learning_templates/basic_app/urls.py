from django.conf.urls import url
from basic_app import views

#TEMPLATE NAME
app_name = 'basic_app'


urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^other/$',views.other,name='other'),
    url(r'^relative/$',views.relative,name='relative'),
]
