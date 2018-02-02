#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# convert_between_unicode_fullwidth_halfwidth_characters.py by greenqy
# url: https://gist.github.com/greenqy/3f153f04de1840500b30e14219a6b4c3

HALF2FULL = dict((i, i + 0xFEE0) for i in range(0x21, 0x7F))
HALF2FULL[0x20] = 0x3000

FULL2HALF = dict((i + 0xFEE0, i) for i in range(0x21, 0x7F))
FULL2HALF[0x3000] = 0x20

def fullen(s):
    '''
    Convert all ASCII characters to the full-width counterpart.
    '''
    return str(s).translate(HALF2FULL)

def halfen(s):
    '''
    Convert full-width characters to ASCII counterpart
    '''
    return str(s).translate(FULL2HALF)
