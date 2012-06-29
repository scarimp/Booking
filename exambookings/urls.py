from django.conf.urls.defaults import *

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import DetailView, ListView
from exambookings.models import *


urlpatterns = patterns('',
    url(r'^$',  # this one is also left over from Poll example App
        ListView.as_view(
            queryset=Poll.objects.order_by('-pub_date')[:5],
            context_object_name='latest_poll_list',
            template_name='exambookings/index.html')),
    url(r'^(?P<pk>\d+)/$',  # this one is left over from Poll example App
        DetailView.as_view(
            model=Poll,
            template_name='exambookings/detail.html')),
    url(r'^(?P<pk>\d+)/results/$',  # this one is left over from Poll example App
        DetailView.as_view(
            model=Poll,
            template_name='exambookings/results.html'),
        name='poll_results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'exambookings.views.vote'), # this one left over from Poll App
    url(r'^static_page/(?P<file_name>.*\.html)$', 'exambookings.views.static_page'), # test out way to serve static page as though it were dynamic
) + static(settings.STATIC_URL, document_root='exambookings/static/')
