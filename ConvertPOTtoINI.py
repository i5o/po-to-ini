#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2014 - Ignacio Rodríguez <ignacio@sugarlabs.org>
# This is for the .pot file.
# How to use: script.py file.pot, it will write a file.ini

import os
import sys


def convert_pot_to_ini(filename):
    filename = sys.argv[1]
    text = open(filename, "r").read()
    lang = os.path.basename(filename)[:-4]  # -4 = .pot
    finaltext = ""

    REPLACE = [
        ",",
        "(",
        ")",
        "?",
        "¿",
        "<",
        ">",
        ".",
        '"\n',
        '"',
        ":",
        "%s",
        "%d",
        "/",
        "'",
        ";",
        "×",
        "¡",
        "!"]

    msgid = text.find("msgid")
    msgstr = text.find("msgstr")
    while msgid >= 0:
        original = text[msgid:msgstr - 1][7:-1]
        got = str(original)
        for x in REPLACE:
            got = got.replace(x, "")

        got = got.replace(" ", "-")
        txt = got + ' = %s\n' % original.replace('\n', ' ').replace('"', '')
        if not txt.startswith(" = "):
            finaltext += txt
        text = text[msgstr:]
        enter = text.find("\n")
        text = text[enter:]
        msgid = text.find("msgid")
        msgstr = text.find("msgstr")

    return finaltext, lang

if __name__ == '__main__':
    ini = convert_pot_to_ini(sys.argv[1])
    text_n = open(ini[1] + ".ini", "w")
    text_n.write(ini[0])
    text_n.close()
    print "Finished"
