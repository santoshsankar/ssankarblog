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
FEED_ALL_RSS = 'feeds/all.rss.xml'

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'))

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/santoshsankar'),)

# static paths will be copied under the same name
STATIC_PATHS = ["images", ]

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISQUS_SITENAME = "Dynamic Thoughts for an Evolving World"
DISQUS_SHORTNAME = "santoshsankar"
DISQUS_NO_ID = "False"
DISQUS_ID_PREFIX_SLUG = 'True'
GOOGLE_ANALYTICS = 'UA-5441380-3'
