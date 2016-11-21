# Copyright (C) 2007-2014 by the Free Software Foundation, Inc.
#
# This file is part of GNU Mailman.
#
# GNU Mailman is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# GNU Mailman is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# GNU Mailman.  If not, see <http://www.gnu.org/licenses/>.

import re
import sys

from setuptools import setup



setup(
    name            = 'mailman-bundler',
    version         = '3.0.0',
    description     = 'Mailman with its admin and archiving interfaces',
    long_description= """\
This is GNU Mailman, a mailing list management system distributed under the
terms of the GNU General Public License (GPL) version 3 or later.
This package installs GNU Mailman alongside its administration and archiving
interfaces, Postorius and HyperKitty.
""",
    author          = 'The Mailman Developers',
    author_email    = 'mailman-developers@python.org',
    license         = 'GPLv3',
    url             = 'http://mailman-bundler.readthedocs.org',
    keywords        = 'email',
    packages        = ['mailman_bundler'],
    include_package_data = True,
    install_requires = [
        "zc.buildout"
        ],
    entry_points = {
        "console_scripts": [
            "django-read-settings = mailman_bundler.django_read_settings:main",
            ],
        },
    )
