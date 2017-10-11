#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'simplynail'
SITENAME = "Pawel's site"
SITEURL = ''

THEME = 'crowsfoot'

PATH = 'content'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'Polish'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#STATIC_PATHS = ['images', 'static_files']

#pelican-blue args
SIDEBAR_DIGEST = 'Programmer and Web Developer'
FAVICON = 'url-to-favicon'
DISPLAY_PAGES_ON_MENU = True
#TWITTER_USERNAME = 'twitter-user-name'
MENUITEMS = (('Blog', SITEURL),)

#crowsfoot theme args
SITESUBTITLE = 'inżynier budowlany, pasjonat IT i programowania'
PROFILE_IMAGE_URL = '/images/avatar.jpg'
EMAIL_ADDRESS = 'cwiek.pawel _on_ gmail.com'
GITHUB_ADDRESS = 'https://github.com/simplynail'
SO_ADDRESS = 'https://stackoverflow.com/users/5769958/simplynail'
SHOW_ARTICLE_AUTHOR = False

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/pawelcwiek'),
          ('github', 'https://github.com/simplynail'),
		  ('stackoverflow', 'https://stackoverflow.com/users/5769958/simplynail'),)

DEFAULT_PAGINATION = 5
SUMMARY_MAX_LENGTH = 300
SLUGIFY_SOURCE = 'title'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
