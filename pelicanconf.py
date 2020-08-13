#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Pawel Cwiek'
SITENAME = 'Pawel Cwiek'
SITEURL = ''

# try 'symlinkthemes' from invoke tasks.py method first  
THEME = 'themes/attila' #good for website 1
#THEME = 'themes/Casper2Pelican' #simmilar to attila
#THEME = 'themes/clean_blog' #good for website 2
#THEME = 'themes/fh5co-marble' # very good, comprehensive sidebar-based theme
#THEME = 'themes/free-agent' # not working one-pager
#THEME = 'themes/minimalX'
#THEME = 'themes/nest' # quite nice sigle pane with big foto headers
#THEME = 'themes/sn_crowsfoot' # simple graphics minimalist one pane blog
#THEME = 'themes/sn_pelican-blue' # neat clean sidebar theme
#THEME = 'themes/twenty-pelican-html5up'

# THEME_TEMPLATES_OVERRIDES = ['themes']
# CSS_FILE = 'main.css'

# --------- theme settings:

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
LI_ADDRESS = 'https://linkedin.com/in/pawelcwiek/'
SHOW_ARTICLE_AUTHOR = False
# --------- theme settings END

PATH = 'content'
USE_FOLDER_AS_CATEGORY = True
DISPLAY_PAGES_ON_MENU = True
PAGE_PATHS = ['pages']
DISPLAY_CATEGORIES_ON_MENU = False

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'pl'

# plugins
PLUGIN_PATHS = ["plugins", "/plugins"]
PLUGINS = ['i18n_subsites','tag_cloud', ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

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