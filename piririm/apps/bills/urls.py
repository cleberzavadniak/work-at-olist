from django.conf.urls import url

from . import views


urlpatterns = [  # pragma: no cover
    url(r'^(?P<source>\w{10,11})$', views.BillEndpoint.as_view(), name='bill'),
    url(r'^charge-entries/$', views.ChargeEntryListEndpoint.as_view(), name='charge-entries-list'),
    url(r'^charge-entries/(?P<pk>\w{26})$', views.ChargeEntryDetailEndpoint.as_view(), name='charge-entries-detail'),
]
