# -*- coding: utf-8 -*-

import multiprocessing
import os
from distutils.util import strtobool

bind = f'0.0.0.0:{os.getenv("FPTRACE_PORT", "5000")}'
print("\nbind value in fptrace gunicorn config: ", bind)
# bind = "0.0.0.0:5000"
accesslog = "-"
access_log_format = (
    "%(h)s %(l)s %(u)s %(t)s '%(r)s' %(s)s %(b)s '%(f)s' '%(a)s' in %(M)sms"  # noqa: E501
)

workers = int(os.getenv("WEB_CONCURRENCY", multiprocessing.cpu_count() * 2))
threads = int(os.getenv("PYTHON_MAX_THREADS", 1))

reload = bool(strtobool(os.getenv("WEB_RELOAD", "false")))
