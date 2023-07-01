from django_hosts import patterns, host
from django.conf import settings

#test
host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'gedus', 'main.urls', name='gedus'),
)