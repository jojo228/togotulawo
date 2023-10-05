from django_hosts import patterns, host
from django.conf import settings


host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'gedus', 'gedus.urls', name='gedus'),
    host(r'numerisation', 'numerisation.urls', name='numerisation'),
    host(r'tdm', 'tdm.urls', name='tdm'),
    host(r'ckeditor_uploader', 'ckeditor_uploader.urls', name='ckeditor_uploader'),
)
