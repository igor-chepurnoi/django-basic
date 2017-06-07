INTERNAL_IPS = ['127.0.0.1', '172.19.0.1', ]

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]
