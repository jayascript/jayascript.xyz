#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jaya Z.'
SITENAME = 'JayaScript'
SITESUBTITLE = 'Linux · Python · Developer · Analytics'
SITEURL = ''

PATH = 'content'
ARTICLE_PATHS = ['posts']
STATIC_PATHS = ['images', 'files']

# http://docs.getpelican.com/en/stable/plugins.html#how-to-use-plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-bootstrapify']

BOOTSTRAPIFY = {
    'table': ['table', 'table-striped', 'table-hover'],
    'img': ['img-fluid'],
    'blockquote': ['blockquote'],
}

TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'
LOCALE = ('en_US.utf8',)
DATE_FORMATS = {
    'en': ('en_US.utf8', '%Y-%m-%d')
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Home', '/'),
    ('Categories', '/categories.html'),
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#----------THEME SPECIFICATIONS----------#

THEME = "themes/pelican-alchemy/alchemy"

THEME_CSS_OVERRIDES = [
    "https://fonts.googleapis.com/css2?family=Raleway:wght@200&display=swap",
]

SITEIMAGE = "/images/data.png"

ICONS = (
    ('github', 'https://github.com/jayascript/'),
    ('twitter', 'https://twitter.com/jayascript'),
    ('linkedin', 'https://www.linkedin.com/in/jayazhane/'),
    ('fa fa-book', 'https://realpython.com/team/jayazhane/'),
)

HIDE_AUTHORS = True
