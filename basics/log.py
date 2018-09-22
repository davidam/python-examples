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
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import logging
import os

# Se crea el nombre del log y se inicializa el logger
ID=datetime.datetime.now().strftime('LOG_%Y%m%d-%Hh%Mm')
logname="/tmp/LOGS/"+ID+".log"
os.makedirs(os.path.dirname(logname), exist_ok=True)
logger = logging.getLogger(__name__)
handler = logging.FileHandler(logname)
formatter = logging.Formatter('%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.error(' cannot be built... maybe source input url is bad...', exc_info=False)
