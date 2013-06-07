#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pwd
import grp

debug = True
test = False

# user name of the user who run decanter
user = pwd.getpwuid(os.getuid()).pw_name

# group name of the user who run decanter
group = grp.getgrgid(os.getegid()).gr_name

# if you run '/path/to/decanter.py', it becomes like '/path/to'
decanterpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# file generated by decanter will be placed here
genpath = os.path.join(decanterpath, 'gen')

# pid file
pidfile = os.path.join(genpath, 'run', 'decanter_{0}.py')

# logging
logger = {
    # log directory path, first {0} is the port number and second {1] is the
    # date
    'filepath': os.path.join(genpath, 'log', 'decanter_{0}-{1}.log'),
    # DEBUG, INFO, WARNING, ERROR, FATAL
    'level': 'DEBUG'
}

# the application directory
apppath = os.path.join(decanterpath, 'app')

# default routes
default = {
    'bundle': 'home',
    'controller': 'index'
}

# list of plugins names to install by default
plugins = ['jinja2']

# redis config settings
redis = {
    'db': 0,
    'host': 'localhost',
    'port': 6379,
    'max_poolsize': 5,
}

# session settings
session = {
    # the cookie key
    'name': 'dev_myGSession',
    # lifetime in seconds. use 0 to have the session last until the
    # browser is closed or up to 24h
    'lifetime': 0,
    # domain under which this session is available
    'domain': 'gengo.andrea',
}

# cookie settings
cookie = {
    'path': '/',
    # a valid cookie domain must start with a dot
    # and must have at least one embedded dot
    # .localhost is not a valid domain it does not
    # have an embedded dot
    # in development mode use None
    'domain': None,
    # only use the cookie over ssl
    'secure': False,
    # use only for http requests, i.e. no javascript
    'httponly': False,
}

# encryption/descryption key, use to encrypt session cookie values
key = 'e77989ed21758e78331b20e477fc5582'
