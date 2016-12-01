#!/usr/bin/python
# coding: utf-8
#
# MicroNovels, copyright (c) 2016 Ben Kybartas <bkybartas@gmail.com>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# 29 November 2014

import random

def get_word_count(novel):
    return len(novel.split())

novel = ""
while(get_word_count(novel) < 50000):

    for i in range(random.randint(5,20)):
        novel += "Went " + random.choice(["North", "South", "East", "West"]) + ". Sand.\n"
    novel += "\"h"

    for i in range(random.randint(1,10)):
        novel += "m"
    novel += "...\"\n"

file = open("PonderingLifeInTheInfiniteDesert.txt", "w")
file.write(novel)
file.close()