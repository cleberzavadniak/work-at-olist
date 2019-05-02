from django.conf.urls import url

from . import views


urlpatterns = [  # pragma: no cover
    url(r'^start/$', views.CallStartRecordListEndpoint.as_view(), name='call-start-records-list'),
    url(r'^start/(?P<pk>\w{26})$', views.CallStartRecordDetailEndpoint.as_view(), name='call-start-records-detail'),

    url(r'^end/$', views.CallEndRecordListEndpoint.as_view(), name='call-end-records-list'),
    url(r'^end/(?P<pk>\w{26})$', views.CallEndRecordDetailEndpoint.as_view(), name='call-end-records-detail'),
]
