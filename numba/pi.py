#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2019  David Arroyo Menéndez

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
# along with pi; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import numba
import numpy as np
import argparse
import time

def calc_pi_single(n):
    x = 2*np.random.ranf(n)-1
    y = 2*np.random.ranf(n)-1
    return 4*np.sum(x**2+y**2<1)/n


run_parallel = numba.config.NUMBA_NUM_THREADS > 1

@numba.njit(parallel=run_parallel)
def calc_pi(n):
    x = 2*np.random.ranf(n)-1
    y = 2*np.random.ranf(n)-1
    return 4*np.sum(x**2+y**2<1)/n

def main():
    parser = argparse.ArgumentParser(description='Calculate Pi.')
    parser.add_argument('--points', dest='points', type=int, default=20000000)
    args = parser.parse_args()
    points = args.points
    np.random.seed(0)

    t1 = time.time()
    pi = calc_pi(points)
    selftimed = time.time()-t1
    print("SELFTIMED ", selftimed)
    print("result: ", pi)

    points_single = args.points
    np.random.seed(0)

    t1_single = time.time()
    pi_single = calc_pi_single(points)
    selftimed_single = time.time()-t1
    print("SELFTIMED ", selftimed_single)
    print("result: ", pi_single)


if __name__ == '__main__':
    main()
