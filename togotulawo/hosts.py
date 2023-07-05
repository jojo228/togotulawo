from django_hosts import patterns, host
from django.conf import settings


host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'gedus', 'main.urls', name='main'),
    host(r'dashboard', 'dashboard.urls', name='dashboard'),
    host(r'entreprise', 'entreprise.urls', name='entreprise'),
)
