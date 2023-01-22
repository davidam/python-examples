#  Copyright (C) 2023 David Arroyo Menendez

#  Author: David Arroyo Menendez <davidarroyomenendez@MacBook-Pro-de-David.local> 
#  Maintainer: David Arroyo Menendez <davidarroyomenendez@MacBook-Pro-de-David.local> 
#  This file is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3, or (at your option)
#  any later version.
# 
#  This file is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
# 
#  You should have received a copy of the GNU General Public License
#  along with python-examples; see the file GPL.txt.  If not, write to
#  the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, 
#  Boston, MA 02110-1301 USA,

import os

dir0 = "files/tmp"
if (not os.path.exists(dir0)):
    print(os.makedirs(dir0))
