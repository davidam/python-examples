#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,
def get_number_of_forks():
    return len(forks)


def get_fork(index):
    return forks[index]


def get_fork_left(index):
    fork = get_fork(index % get_number_of_forks())
    if fork:
        return fork
    else:
        return get_fork(len(forks) - 1)


def get_fork_right(index):
    fork = get_fork((index + 1) % get_number_of_forks())
    if fork:
        return fork
    else:
        return get_fork(len(forks) - 1)


forks = [['localhost', 4000],
         ['localhost', 4001],
         ['localhost', 4002],
         ['localhost', 4003],
         ['localhost', 4004]]
