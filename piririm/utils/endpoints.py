from powerlibs.django.restless.modelviews import ListEndpoint, DetailEndpoint
from powerlibs.django.restless.contrib.endpoints import (BaseEndpointMixin,
                                                         PaginatedEndpointMixin,
                                                         FilteredEndpointMixin,
                                                         OrderedEndpointMixin)


class CommonListEndpoint(BaseEndpointMixin,
                         PaginatedEndpointMixin,
                         FilteredEndpointMixin,
                         OrderedEndpointMixin,
                         ListEndpoint):
    methods = ['GET', 'POST']


class CommonDetailEndpoint(BaseEndpointMixin,
                           DetailEndpoint):
    methods = ['GET', 'POST']
