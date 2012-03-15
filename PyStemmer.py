#-*- coding: UTF-8 -*-
"""Norwegian stemming algorithm.

This is a python port of the Java snowball: http://snowball.tartarus.org/algorithms/norwegian/stemmer.html
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


__author__ = "Morten Goodwin"
__version__ = "$Revision$"
__updated__ = "$LastChangedDate: 2009-05-08 15:19:38 +0000 (Fri, 08 May 2009) $"

def lengthsort(x,y):
    return cmp(len(x),len(y))

firstsuffixes = "a   e   ede   ande   ende   ane   ene   hetene   en   heten   ar   er   heter   as   es   edes   endes   enes   hetenes   ens   hetens   ers   ets   et   het   ast".split()
firstsuffixes.sort(lengthsort,reverse=True)
secondsuffixes = "leg   eleg   ig   eig   lig   elig   els   lov   elov   slov   hetslov".split()
secondsuffixes.sort(lengthsort,reverse=True)

valids = "b   c   d   f   g   h   j   l   m   n   o   p   r   t   v   y   z".split()

vowels = 'a e i o u u ø å æ'

def stemword(word):
    if len(word)==1:
        return word
    changed = False
    for suffix in firstsuffixes:
        if not changed:
            if word.endswith(suffix):
                try:
                    if not (word[:-len(suffix)].endswith('k') and (word[:-len(suffix)][-2] in vowels)):
                         word = word[:-len(suffix)]
                except IndexError,e:
                    word = word
                changed = True
    if not changed:
        for valid in valids:
            valid = valid + 's'
            if word.endswith(valid):
                word = word[:-1]
    if not changed:
        if word.endswith('k') and not word[-2] in vowels:
             word = word[:-1]
    for suffix in ('erte','ert'):
        if word.endswith(suffix):
            word = word[:-len(suffix)]
            word = word + 'er'
    if word.endswith('&oslash;ke'):
            word = word[:-1]
    if word.endswith('dt') or word.endswith('vt'):
        word = word[:-1]
    for suffix in secondsuffixes:
        if word.endswith(suffix):
              word = word[:-len(suffix)]
    return word
