#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'moopless'
SITENAME = u'1709 Brewing'
SITEURL = 'https://beer.moopless.com'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
         #('Python.org', 'http://python.org/'),
         #('Jinja2', 'http://jinja.pocoo.org/'),
         #('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
          #('Another social link', '#'),)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
# THEME
THEME = "pelican-themes/pelican-bootstrap3"
DISPLAY_TAGS_INLINE=True
DISPLAY_RECENT_POSTS_ON_SIDEBAR=True
DISPLAY_CATEGORIES_ON_SIDEBAR=True
REVERSE_CATEGORY_ORDER = True
SUMMARY_MAX_LENGTH = None
JINJA_EXTENSIONS = ['jinja2.ext.i18n']
PLUGIN_PATHS = ['pelican-plugins'] 
PLUGINS = ['i18n_subsites']
