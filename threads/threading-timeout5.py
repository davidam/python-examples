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
from threading import Thread, Event
import time
 
 
# Event object used to send signals from one thread to another
stop_event = Event()
 
 
def do_actions():
    """
    Function that should timeout after 5 seconds. It simply prints a number and waits 1 second.
    :return:
    """
    i = 0
    while True:
        i += 1
        print(i)
        time.sleep(1)
 
        # Here we make the check if the other thread sent a signal to stop execution.
        if stop_event.is_set():
            break
 
 
if __name__ == '__main__':
    # We create another Thread
    action_thread = Thread(target=do_actions)
 
    # Here we start the thread and we wait 5 seconds before the code continues to execute.
    action_thread.start()
    action_thread.join(timeout=5)
 
    # We send a signal that the other thread should stop.
    stop_event.set()
 
    print("Hey there! I timed out! You can do things after me!")
