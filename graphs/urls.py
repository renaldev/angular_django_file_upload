from django.conf.urls import url
from graphs.views import GraphDataCreateView, GraphDataView

urlpatterns = [
    url(r'^new/$', GraphDataCreateView.as_view(), name='graphdata-add'),
    url(r'^api/file/(?P<pk>[0-9]+)/$', GraphDataView.as_view(), name='view-one'),
    url(r'^api/file/(?P<pk>[0-9]+)/detail/$', GraphDataView.as_view(with_file_contents = True), name='view-one-detail')
]