#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'liukeyou@gmail.com'
SITENAME = u'bigdata'
SITEURL = '.'
SITELOGO = 'images/favicon.png'
SITELOGO_SIZE = 30

BANNER_SUBTITLE = 'Xdrv.com'

TIMEZONE = 'Asia/Shanghai'
    
PATH = 'content'
THEME = 'pelican-bootstrap3'

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
DISPLAY_TAGS_INLINE = True
DISPLAY_TAGS_ON_SIDEBAR = True
BOOTSTRAP_NAVBAR_INVERSE = True
#DISPLAY_ARTICLE_INFO_ON_INDEX = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'

# Social widget
SOCIAL = (('github', 'http://github.com/liukeyou'),
          ('weibo', 'http://weibo.com/324426767'),
          ('twitter', 'http://twitter.com/liukeyou'),
          )

LINKS = (('hadoop-wireshark', 'http://github.com/liukeyou/hadoop-wireshark'),
          ('hadoop-ansible', 'http://github.com/liukeyou/hadoop-ansible'),
          ('hadoop-loginsight', 'http://github.com/liukeyou/hadoop-loginsight'),)

DEFAULT_PAGINATION = 5
TAG_CLOUD_MAX_ITEMS = 5
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

FAVICON = 'images/favicon.png'
THEME_STATIC_PATHS = ['static','images']

STATIC_PATHS = ['images', 'extra/custom.css']
CSS_FILE = 'static/custom.css'
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'}
}

GOOGLE_ANALYTICS = 'UA-22591689-1'


