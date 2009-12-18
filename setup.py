#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2009 Clóvis Fabrício Costa

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Python smbclient wrapper.

This is a wrapper that works by running the "smbclient" subprocess and providing
an API similar to the one provided by python `os` module.

It is an ugly hack, but it is here for anyone that finds it useful.

The programmer before me was using a "bash" file with lots of smbclient calls, 
so I think my solution is at least better.

Usage example:

>>> smb = smbclient.SambaClient(server="MYSERVER", share="MYSHARE", 
                                username='foo', password='bar', domain='baz')
>>> print smb.listdir("/")
[u'file1.txt', u'file2.txt']
>>> f = smb.open('/file1.txt')
>>> data = f.read()
>>> f.close()
>>> smb.rename(u'/file1.txt', u'/file1.old')
"""

from distutils.core import setup

setup(name='PySmbClient',
          version='0.1.2',
          description="A convenient smbclient wrapper",
          long_description=__doc__,
          author="nosklo",
          author_email="bucket.t.nosklo@0sg.net",
          url='http://bitbucket.org/nosklo/pysmbclient',
          classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Operating System :: POSIX',
            'Programming Language :: Python :: 2.6',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: System :: Filesystems',
            'Topic :: System :: Networking',
            'Topic :: Utilities',
          ],
          py_modules=['smbclient'],
      )
      

