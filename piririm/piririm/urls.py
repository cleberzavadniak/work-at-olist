from django.conf.urls import url, include


urlpatterns = [
    url(r'^v1/bills/', include('apps.bills.urls')),
    url(r'^v1/records/', include('apps.records.urls')),
]
