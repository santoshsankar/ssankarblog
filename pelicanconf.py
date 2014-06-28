#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Santosh Sankar'
SITENAME = u'Dynamic Thoughts for an Evolving World'
SITEURL = ''

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

TIMEZONE = 'America/New_York'
DATE_FORMATS = {
    'en': '%a, %d %b %Y',
}

DEFAULT_LANG = u'en'

THEME = 'pelican-bootstrap3'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'))

# Social widget
SOCIAL = (('@santoshsankar', 'http://www.twitter.com/santoshsankar'),)

# static paths will be copied under the same name
STATIC_PATHS = ["images", ]

PLUGINS = [u"disqus_static"]

DISQUS_SITENAME = u'santoshsankar'
DISQUS_SECRET_KEY = u'oWGk5VpD0rzLaszm23TMkyvuAVp3J9dnMEA4r5v3jXMkp4ufKLFUQtYYGwHsbuCl'
DISQUS_PUBLIC_KEY = u'dXFuVr4UFuykiZWYOnhvPfGD06D571dKLSFEZgWQujiJWkDIkpC91QaT6X0rs0YR'

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
