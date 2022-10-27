# -*- coding: utf-8 -*-


from setuptools import find_packages
from setuptools import setup

import fastentrypoints

dependencies = []

config = {
    "version": "0.1",
    "name": "delay-timer",
    "url": "https://github.com/jakeogh/delay-timer",
    "license": "ISC",
    "author": "Justin Keogh",
    "author_email": "github.com@v6y.net",
    "description": "Short explination of what it does _here_",
    "long_description": __doc__,
    "packages": find_packages(exclude=["tests"]),
    "include_package_data": True,
    "zip_safe": False,
    "platforms": "any",
    "install_requires": dependencies,
    "entry_points": {
        "console_scripts": [
            "delay-timer-test=delay_timer.delay_timer_test:cli",
        ],
    },
}

setup(**config)
