#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2020 Tobias Gruetzmacher
'''update languages.py from pycountry'''
import os
import codecs

from dosagelib.scraper import get_scrapers


def main():
    """Update language information in dosagelib/languages.py."""
    basepath = os.path.dirname(os.path.dirname(__file__))
    fn = os.path.join(basepath, 'dosagelib', 'languages.py')
    with codecs.open(fn, 'w', 'utf-8') as f:
        f.write('# SPDX-License-Identifier: MIT\n')
        f.write('# ISO 693-1 language codes from pycountry\n')
        f.write('# This file is automatically generated, DO NOT EDIT!\n')
        lang = get_used_languages()
        write_languages(f, lang)


def get_used_languages():
    languages = {}
    for scraperobj in get_scrapers():
        lang = scraperobj.lang
        if lang not in languages:
            languages[lang] = scraperobj.language()
    return languages


def write_languages(f, lang):
    """Write language information."""
    f.write("Languages = {%s" % os.linesep)
    for lang in sorted(lang):
        f.write("    %r: %r,%s" % (lang, lang[lang], os.linesep))
    f.write("}%s" % os.linesep)


if __name__ == '__main__':
    main()
