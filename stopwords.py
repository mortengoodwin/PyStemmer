#-*- coding: UTF-8 -*-
"""List of stopwords

Id$
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

__version__ = "$Revision$"
__updated__ = "$LastChangedDate: 2009-05-08 15:19:38 +0000 (Fri, 08 May 2009) $"

import string
import sc
import os
sc = sc.SystemConfiguration()

stopwords = [i.strip() for i in open('stopwords').readlines()]

nonasciiwords = ['-','=','}','{','+','/',':','|','>',',','"','\'',')','(','[',']','_','%','.']

def heavystrip(input):
    retwords = {}
    for word,value in input.items():
        retword = ''
        for character in word.lower():
            if character in string.ascii_lowercase + 'øæå&;':#'1234567890øæåi&;':
                retword += character
        if retword:
            retwords[retword]=value
    return retwords


def withinstopword(input):
    if not input.strip():
        return True
    if input.lower() in stopwords:
        return True
    else:
        return False


def removestopwords(input):
    if type(input)==type([]):
        for word in stopwords:
            while word in input:
                input.remove(word)
        return input
    if type(input)==type({}):
        for word in stopwords:
            try:
                input.pop(word)
            except KeyError:
                pass
        return input
    if input in stopwords:
        return ''
    return input

def removenonascii(input):
    for word in input.keys():
        if not word.strip():
             input.pop(word)
        for nonascii in nonasciiwords:
             if nonascii in word:
                 try:
                     input.pop(word)
                 except KeyError:
                     pass
        isok = False
        for value in string.ascii_lowercase + '1234567890æøå&;':
            if value in word:
                isok = True
        try:
            int(word)
            isok = False
        except ValueError:
            pass
        try:
            int(word[0])
            isok = False
        except ValueError:
            pass
        if not isok:
            try:
                input.pop(word)
            except KeyError:
                pass

    return input


