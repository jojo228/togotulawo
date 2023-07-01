from django_hosts import patterns, host
from django.conf import settings


host_patterns = patterns('',
    host(r'', settings.ROOT_URLCONF, name=' '),
    host(r'gedus', 'main.urls', name='main'),
    host(r'account', 'account.urls', name='account'),
    host(r'dashboard', 'dashboard.urls', name='dashboard'),
    host(r'entreprise', 'entreprise.urls', name='entreprise'),
)
