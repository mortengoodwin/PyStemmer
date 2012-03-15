""" Installation for PyStemmer

$Id$
"""

#      Copyright 2008-2012 Morten Goodwin
#      This program is distributed under the terms of the GNU General
#      Public License.
#
#  This file is part of the PyStemmer
#
#  PyStemmer is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  PyStemmer is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with PyStemmer; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston,
#  MA 02110-1301 USA


__author__ = "Morten Goodwin"
__version__ = "$Revision$"
__updated__ = "$LastChangedDate$"



import sys
from distutils.core import setup
import shutil
import sys
import os

if 'install' in sys.argv:
   print 'Installing'

   setup(name = "PyStemmer",
      version="0.1",
      description="Norwegian Stemming",
      author="Morten Goodwin",
      author_email="mortengoodwin@gmail.com",
      url="http://mortengoodwin.net",
      license="GNU General Public License 2",
      py_modules=['PyStemmer','stopwords'])

