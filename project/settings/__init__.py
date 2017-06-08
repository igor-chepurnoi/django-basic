from split_settings.tools import optional, include

include(
    'base/env.py',
    optional('local/env.py'),

    # Here we should have the order because of dependencies
    'base/common.py',
    'base/db.py',
    'base/security.py',
    'base/middleware.py',
    'base/debug_toolbar.py',
    'base/emails.py',

    # we can load any other settings from local folder
    optional('local/*.py'),
)
