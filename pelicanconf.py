#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jon'
SITENAME = u'Jon Staley'
SITEURL = 'jonstaley.co.uk'

THEME='droidstrap'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PROFILE_IMG_URL='/images/avatar.png'

STATIC_PATHS=['images', 'extra/CNAME', 'docs']
EXTRA_PATH_METADATA={'extra/CNAME': {'path': 'CNAME'},}

OUTPUT_PATH = 'output'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
PAGE_URL = 'output/{slug}.html'
PAGE_SAVE_AS = 'output/{slug}.html'
MENUITEMS = []
